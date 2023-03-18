#from dotenv import load_dotenv
import os
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
import message_handlers

#load_dotenv()


def main():
    application = ApplicationBuilder().token( os.environ.get('BOT_TOKEN') ).build()
    
    #declaration of message handlers
    on_message = MessageHandler(filters.TEXT & (~filters.COMMAND), message_handlers.on_message)
    on_start = CommandHandler('start', message_handlers.start)

    #message handlers
    application.add_handler(on_start)
    application.add_handler(on_message)
    
    #start bot
    application.run_polling()


if __name__ == "__main__":
    main()