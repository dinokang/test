#!/usr/bin/python3

import openai
import sys
import argparse

# Define OpenAI API key
openai.api_key = "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"


# Set up the model and prompt
model_engine = 'text-davinci-003'
prompt = "what is banana?"
# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print("Answer : " + response)


