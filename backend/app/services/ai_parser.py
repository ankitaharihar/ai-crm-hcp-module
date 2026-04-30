from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def parse_interaction(text: str):
    print("INPUT:", text)

    response = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {"role": "user", "content": f"Summarize this: {text}"}
        ]
    )

    content = response.choices[0].message.content
    print("OUTPUT:", content)

    return {
        "result": content
    }