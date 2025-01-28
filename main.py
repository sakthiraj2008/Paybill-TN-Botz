from pyrogram import Client, filters


API_ID = "11472991"
API_HASH = "c78c50d54baf2173e8b3f75c359c0c72"
BOT_TOKEN = "7849658420:AAFtkZoP-knEMgquZQuMnKbGdd7tOQwrS1A"

TnBotz = Cilent(
     name="Payment_TN_Bot", 
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
