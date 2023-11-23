from openai import OpenAI

client = OpenAI(
    api_key="sk-YOUR OPENAI KEY"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "You are helpful assistant."},
    {"role": "user", "content": "hello. json"}
  ],
  response_format={"type": "json_object"}
)

print(completion.choices[0].message.content)