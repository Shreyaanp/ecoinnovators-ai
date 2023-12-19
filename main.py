from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import logging
import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd
import glob
from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure logging
logging.basicConfig(
    filename="conversation_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

# FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    prompt: str

class DataPrompt(BaseModel):
    dataframe_name: str
    question: str

# Load all CSV files from the 'data' directory
def load_all_csv_files(directory):
    csv_files = glob.glob(os.path.join(directory, '*.csv'))
    file_paths = {}
    for file in csv_files:
        df_name = os.path.basename(file).split('.')[0]
        file_paths[df_name] = file  # Store the file path
    return file_paths

all_csv_file_paths = load_all_csv_files('./data')

@app.post("/generate-response/")
async def generate_response(prompt: Prompt):
    try:
        bot = ConversationBot()
        bot_response = bot.get_openai_response(prompt.prompt)
        logging.info(f"User: {prompt.prompt}")
        logging.info(f"Bot: {bot_response}")
        return {"bot_response": bot_response}
    except Exception as e:
        logging.error(f"Error in generating response: {e}")
        return {"error": "An error occurred while processing your request"}

@app.post("/talkdata/")
async def talk_to_data(prompt: DataPrompt):
    try:
        if prompt.dataframe_name not in all_csv_file_paths:
            return {"error": "CSV file not found"}

        # Use the file path of the specified CSV file for the agent
        csv_file_path = all_csv_file_paths[prompt.dataframe_name]
        agent = create_csv_agent(OpenAI(temperature=0),
                                 csv_file_path,  # Pass the file path
                                 verbose=True)

        agent_response = agent.run(prompt.question)
        return {"response": agent_response}
    except Exception as e:
        logging.error(f"Error in talking to data: {e}")
        return {"error": "An error occurred while processing your request"}

class ConversationBot:
    def __init__(self):
        self.conversation_state = {"messages": []}
    def get_openai_response(self, message):
        headers = {
            "Authorization": f"Bearer {openai.api_key}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "gpt-4-1106-preview",
            "max_tokens": 150,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an helpful data scientist who is trying to help a user with a problem."
                        "you can reply to user for thank you, sure and no problem.e "
                        "you dont have to reply the user with code, rather if possible execute it and then show the data. If not then just reply with suggestions on doing the task"

                    ),
                },
            ]
            + self.conversation_state["messages"]
            + [{"role": "user", "content": message}],
        }

        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                data=json.dumps(data),
            )
            if response.status_code != 200:
                logging.error(
                    f"API call failed with status code {response.status_code} and message: {response.text}"
                )
                return "Sorry, I encountered an error with the API call."

            response_data = response.json()
            if "choices" not in response_data or not response_data["choices"]:
                logging.error("No 'choices' field in the API response.")
                return "Sorry, I encountered an error with the response format."

            bot_message = response_data["choices"][0]["message"]["content"]
            if not bot_message.strip():
                logging.info("Received empty response from API")
                return "I'm not sure how to respond to that. Could you clarify or ask something else?"

            return bot_message

        except Exception as e:
            logging.error(f"Error in calling OpenAI API: {e}")
            return "Sorry, I encountered an error. Could you repeat that?"