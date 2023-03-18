from telegram import Update
from telegram.ext import ContextTypes
import chatgpt_client


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Chatty AI is an AI-powered chatbot that uses the OpenAI GPT. \n"+
            "Let's get started!")


async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    ai_response = chatgpt_client.generate_response( update.message.text)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=ai_response)