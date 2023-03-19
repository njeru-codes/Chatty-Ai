from pymongo import MongoClient
from dotenv import load_dotenv
import os, pymongo
from datetime import datetime

load_dotenv()

async def create_connection():
    try:
        client = MongoClient( os.environ.get('MONGO_URI') )
        print('db connected')
        return client
    except Exceptionas as error:
        print( error)
        return


async def insert_message(chat_id, message):
    try:
        client = await create_connection()
        database = client.chatty_ai
        collection = database.messages

        message ={
            "chat_id": chat_id,
            "message": message,
            "created": datetime.now()
        }
        message_id = collection.insert_one(message).inserted_id
        client.close()
        
    except Exception as error:
        print(error)


async def get_messages(chat_id):
    try:
        client = await create_connection()
        database = client.chatty_ai
        collection = database.messages


        if collection.count_documents({"chat_id": chat_id}) <= 0:
            print( 'no messages were found for chat')
            return None

        db_messages = collection.find( {"chat_id": chat_id}).sort( [('created', pymongo.DESCENDING)] ).limit(12)
        messages =[]
        for message in db_messages:
            messages.append(message['message'])
        client.close()
        return messages
    except Exception as error:
        print(error)


