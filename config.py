import os
from dotenv import load_dotenv
from dune_client.client import DuneClient

# Set the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))

# Specify the directory where the .env file is located
dotenv_path = os.path.join(project_root, "../.env")

# Load the .env file
load_dotenv(dotenv_path=dotenv_path)
print("Environment variables are loaded.")

# Check if the environment variable is loaded
api_key = os.getenv("DUNE_API_KEY")
if api_key:
    print(f"DUNE_API_KEY connect completed.")
else:
    print("DUNE_API_KEY not found. Please check the .env file and path.")

# Set up the DuneClient, proceed only if environment variables are confirmed
if api_key:
    dune = DuneClient.from_env()
    print("DuneClient is set up.")
