from pyrogram import Client, filters


API_ID = "11472991"
API_HASH = "c78c50d54baf2173e8b3f75c359c0c72"
BOT_TOKEN = "7238940586:AAHnEBgiRloqtZyGd3IPAyPGS01d2g8Jr4A"


TnBotz = Cilent(
     name="PayBill_UPI_Bot", 
     api_id=API_ID, 
     api_hash=API_HASH, 
     bot_token=BOT_TOKEN
) 


@TnBotz.on_message(filters.command("start")) 
async def start_cmd(client, message):
     await meaasge.replay_photo(
          photo="https://envs.sh/EyO.jpg",
          caption="ʜᴇʟʟᴏ {}, ᴍʏ ɴᴀᴍᴇ {} 👋, ɪ ᴀᴍ ʟᴀᴛᴇꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ʙᴏᴛ ᴀɴᴅ ʙᴇꜱᴛ ᴜɪ ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇ ")



Print("Bot Was Started") 

TnBotz.run() 
