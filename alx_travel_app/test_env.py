# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()
print("DB_NAME:", os.getenv('DB_NAME'))
print("DB_USER:", os.getenv('DB_USER'))
print("DB_PASSWORD:", os.getenv('DB_PASSWORD'))