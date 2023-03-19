# Chatty Ai

Chatty AI is an AI-powered telegram chatbot that uses the OpenAI GPT models to generate responses to your messages.

test the live bot here https://web.telegram.org/k/#@itsAi_bot

# GETTING  STARTED
create a bot using telegrams @botfather , an API token for OpenAi and and mongoDb connection string
1. create a .env file with the following parameters
    ```
    BOT_TOKEN="**********"
    OPENAI_API_KEY="************"
    MONGO_URI="************"
    ```
2. install the dependencies
    ```
        pip install -r requirements.txt
    ```
3. Start the bot 
    ```
        python app/main.py
    ```