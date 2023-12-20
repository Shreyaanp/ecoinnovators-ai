from pandasai import SmartDataframe
import pandas as pd
from pandasai.helpers import path
import os
from dotenv import load_dotenv
from pandasai.llm import OpenAI
from matplotlib import pyplot as plt
# Load environment variables from .env file
load_dotenv()
plt.ioff()
# Retrieve OpenAI API key from environment variables
api_token = os.getenv('OPENAI_API_KEY')

# Your existing code for reading the CSV file
csv_file_path = './Dataa/prod.csv'
df = pd.read_csv(csv_file_path)

# Rest of your existing code
try:
    user_defined_path = path.find_project_root()
except ValueError:
    user_defined_path = os.getcwd()

# Initialize the LLM with the API token from the environment
llm = OpenAI(api_token=api_token)

# Continue with your existing SmartDataframe configuration
user_defined_path = os.path.join(user_defined_path, "exports", "charts")
df = SmartDataframe(
    df,
    config={
        "llm": llm,
        "save_charts_path": user_defined_path,
        "save_charts": True,
        "verbose": True,
    },
)

# Perform the analysis
response = df.chat("can you perform some predictive analysis on the data?")
