from pyrogram import Client, filters
import re
import os
from os import environ
from Script import script


API_ID = "11472991"
API_HASH = "c78c50d54baf2173e8b3f75c359c0c72"
BOT_TOKEN = "7238940586:AAHnEBgiRloqtZyGd3IPAyPGS01d2g8Jr4A"

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS','7188069786').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "Paybill_UPI_BOT") # without @
PORT = environ.get("PORT", "8080")

DB_URI = environ.get("DB_URI", "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "techvjbotz")

TnBotz = Cilent(
     name="PayBill_UPI_Bot", 
     api_id=API_ID, 
     api_hash=API_HASH, 
     bot_token=BOT_TOKEN
) 


@TNBotz.on_message(filters.command("start")) 
async def start_cmd(client, message):
     print("START Command"):


@TnBotz.on_message(filters.command("help")) 
async def help_cmd(client, message):
     print("Help Command") 


Print("Bot Was Started") 

TnBotz.run() 
