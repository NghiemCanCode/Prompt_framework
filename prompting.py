import os
from openai import OpenAI
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

SYSTEM_CONTENT = "Bạn là một chuyên gia phân tích ngôn ngữ."

open_ai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
google_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def open_ai_prompt(sentence, prompt_template, model="gpt-4o-mini"):
    completion = open_ai_client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system", "content": SYSTEM_CONTENT,
            },
            {
                "role": "user",
                "content": prompt_template.replace("#123123123", sentence)
            }
        ]
    )

    return completion.choices[0].message.content
