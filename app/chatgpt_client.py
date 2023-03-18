import openai
# from dotenv import load_dotenv
import os

#load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')

def generate_response(message):
    prompt = f"User: {message}\nBot:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

