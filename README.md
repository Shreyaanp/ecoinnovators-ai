ChemD
Overview
Welcome to ChemD! This project is a powerful tool that combines the capabilities of the pandasai library and power of large language model to enhance data analysis and exploration. Whether you're a data scientist, analyst, or enthusiast, this tool aims to make your data-driven tasks more intuitive and efficient.

Key Features:

SmartDataframe Integration: The pandasai library empowers you with SmartDataframe, allowing for advanced data manipulation, analysis, and transformation with the simplicity of pandas.
OpenAI Chat-based Analysis: Engage in chat-based interactions powered by OpenAI's GPT model. Interact with your data using natural language queries for a seamless exploration experience.
Automatic Chart Generation: Let the tool automatically generate insightful charts based on your queries and data analysis, providing visualizations that aid in understanding complex datasets.

Installation

Follow these step-by-step instructions to install and set up your project:

Step 1: Clone the Repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

Step 2: Set Up a Virtual Environment (Optional but Recommended)
Create and activate a virtual environment to isolate project dependencies:
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Step 3: Install Dependencies
Install the necessary Python packages listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
Step 4: Set Up Environment Variables
Create a .env file in the project root directory and add your LLM Model key:
env
LANGUAGE_MODEL_API_KEY=your_language_model_api_key_here
Replace your_language_model_api_key_here with your actual API key.

Step 5: Update CSV File Path
In analysis_script.py, update the csv_file_path variable with the path to your CSV file:
csv_file_path = '/path/to/your/csv/file.csv'

Step 6: Run the Script
Run the analysis script to initiate the SmartDataframe and perform analysis using OpenAI chat-based interactions:
python analysis_script.py

Step 7: View Generated Charts
Check the exports/charts directory for automatically generated charts. Explore visualizations that provide insights into your data.

Project Structure
Explore the purpose of key files and directories in your project:
exports/charts/: Directory containing automatically generated charts for visual analysis.
.gitignore: Specifies patterns excluded from version control (Git) to keep the repository clean. Prevents unnecessary files and directories from being tracked.
conversation_log.txt: Log file capturing conversation-related information and interactions. Useful for tracking user queries and responses during analysis.
main.py: The main Python script serving as the entry point for your application. Modify this file to customize the behavior of your tool.
pandasai.log: Log file for the pandasai library, useful for debugging and analysis. It may contain information related to data transformations and SmartDataframe operations.
requirements.txt: Lists project dependencies and their versions for reproducibility. Ensures that others can recreate the same environment.
test.py: Python script dedicated to testing purposes. Includes unit tests or other testing-related code to maintain code quality.
tt.py: Another Python script; purpose not specified. Ensure it aligns with your project goals, or consider providing more information.
vercel.json: Configuration file for Vercel deployment, if applicable. Custom settings for deploying your application on Vercel.
Contributing

Encourage contributions and provide information on how others can contribute to the project:
Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are highly appreciated! Before contributing, please review our Contribution Guidelines.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
