from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def parse_interaction(text: str):
    prompt = f"""
Convert this medical sales interaction into strict JSON.

Return ONLY JSON. No explanation.

Fields:
- hcp_name
- product
- sentiment (positive/neutral/negative)
- summary
- follow_up

Text:
{text}
"""

    response = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {"raw_output": content}