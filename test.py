from dotenv import load_dotenv
import os

load_dotenv()
print("PERPLEXITY_API_KEY:", os.getenv("PERPLEXITY_API_KEY"))
