#!/usr/bin/env -S poetry run python

from openai import OpenAI

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI()

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)
print(completion.choices[0].message.content)
