import re
from pdfminer.high_level import extract_pages, extract_text
import openai
import sys

openai.api_key = ""

model_engine = "gpt-3.5-turbo"


# Read file paths from command-line arguments
file1_path = sys.argv[1]  # Path to student's answer
file2_path = sys.argv[2]  # Path to solution manual

# Read the content of the files
with open(file1_path, "rb") as file1:
    text1 = extract_text(file1)

with open(file2_path, "rb") as file2:
    text2 = extract_text(file2)

#text1 = extract_text("file1")  # I want file1 to be the student's answer uploaded in uploads_1 directory
#text2 = extract_text("file2")  # I want file2 to be the solution manual uploaded in uploads_2 directory
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
