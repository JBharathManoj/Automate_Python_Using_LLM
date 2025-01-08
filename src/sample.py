import openai
import requests
from openai import api_requestor

openai.api_key = "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"

# Disable SSL verification (not recommended for production)
api_requestor._verify_ssl_certs = False

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "what is the smallest bird in the earth"}
  ],
  temperature=0.5,
  max_tokens=100
)

print(response.choices[0].message['content'].strip())