from telegram import Update
from telegram.ext import ContextTypes
import chatgpt_client , database


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Chatty AI is an AI-powered chatbot that uses the OpenAI GPT. \n"+
            "Let's get started!")


async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    messages = await database.get_messages( update.effective_chat.id )
    if messages != None:
        prompt = '\n'.join(messages+ [ update.message.text])
    else:
        prompt = update.message.text
    
    ai_response = chatgpt_client.generate_response( prompt)
    
    await database.insert_message(update.effective_chat.id, update.message.text)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=ai_response)