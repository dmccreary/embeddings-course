import os
from dotenv import load_dotenv

load_dotenv()

MY_ENV_VAR = os.getenv('OPENAI_API_KEY_HOLDER')
print(MY_ENV_VAR)