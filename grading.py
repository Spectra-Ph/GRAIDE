import re
from pdfminer.high_level import extract_pages, extract_text
import openai

openai.api_key = "YOUR_API_KEY"

model_engine = "gpt-3.5-turbo"


text1 = extract_text("file1")
text2 = extract_text("file2")
prompt = "Here is the student's answer: \n" + text1 + "\nAnd here is the solution manual: \n" + text2 + "\n Grade the student according to the solution manual"

# Define your conversation context
conversation = [
    {"role": "system", "content": "You are a helpful assistant that grades student answers."},
    {"role": "user", "content": "Here is the student's answer: \n" + text1},
    {"role": "assistant", "content": "And here is the solution manual: \n" + text2 + "\n"},
    {"role": "user", "content": "Grade the student according to the solution manual (one number answer plz)"}
]

try:
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=conversation,
        max_tokens=1024,
        temperature=0.5,
    )
    print(response['choices'][0]['message']['content'])
except Exception as e:
    print(f"An error occurred: {e}")
