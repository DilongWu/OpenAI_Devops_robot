import os
import openai


openai.api_key = ""

prompt = "how far away between Shanghai and Wuxi"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=10,
    temperature=0.5,
    stop="."
)

print(response["choices"][0]["text"])