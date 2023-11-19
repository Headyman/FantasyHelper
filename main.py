from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()



completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a 1980s rapper."},
    {"role": "user", "content": "Compose a rap song for me."}
  ]
)

print(completion.choices[0].message)