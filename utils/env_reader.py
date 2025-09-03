from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

def get_env_variable(key: str):
    return os.getenv(key)