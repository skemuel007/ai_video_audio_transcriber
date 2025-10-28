import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
TRANSCRIPTS_DIR = os.getenv('TRANSCRIPT_DIR', '/transcripts')

os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)