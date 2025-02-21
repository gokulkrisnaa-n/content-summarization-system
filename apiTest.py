__author__ = 'gokulkrisnaa-n'

# Importing required libraries for the GPT API call
from openai import OpenAI
import os
from dotenv import load_dotenv


def print_conversation(prompt, response):
    print(f'User: {prompt}\nGPT:{response}')


# Loading API keys from the .env file
load_dotenv()

gpt_api_key = os.getenv("GPT_API_KEY")

# Creating instance for OpenAI API
client = OpenAI(api_key=gpt_api_key)

# User prompt
content = """
Summarize the following content: John Doe went to grocery shop.
He bought pancakes, pizza, salsa, and all-purpose flour.
He was trying to make breakfast.
"""

# Sending the prompt to GPT model using the API call
completion = client.chat.completions.create(
    model='gpt-4o-mini',
    store=True,
    messages=[
        {'role': 'user', 'content': content}
    ]
)

print_conversation(content, completion.choices[0].message.content)
