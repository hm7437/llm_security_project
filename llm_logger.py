import os 
import json
from datetime import datetime
from groq import Groq

client = Groq(api_key="your api key")

def ask_and_log(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user", "content": prompt}]
    )
    answer = response.choices[0].message.content
    log_entry = {
        "timestamp": datetime.now().isoformat(), 
        "prompt": prompt,
        "response": answer
    }
    with open("log.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    print("PROMPT:", prompt)
    print("RESPONSE:", answer)
    print("---")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    ask_and_log(user_input)
