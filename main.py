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


@TNBotz.on_message(filters.command("start")) 
async def start_cmd(client, message):
     await meaasge.replay_photo(
          photo="https://envs.sh/EyO.jpg",
          caption="ʜᴇʟʟᴏ {}, ᴍʏ ɴᴀᴍᴇ {} 👋, ɪ ᴀᴍ ʟᴀᴛᴇꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ʙᴏᴛ ᴀɴᴅ ʙᴇꜱᴛ ᴜɪ ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇ ")


@TnBotz.on_message(filters.command("about")) 
async def about_cmd(client, message):
     await message.replay(
              ABOUT_TXT = """<b>ʜɪ ɪ ᴀᴍ ᴘᴇʀᴍᴀɴᴇɴᴛ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡɪᴛʜ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ + ᴄᴜsᴛᴏᴍ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ɪᴛ ᴍᴇᴀɴs ᴀɴʏ ᴜsᴇʀ ᴄᴀɴ sᴇᴛ ʜɪs ᴜʀʟ sʜᴏʀᴛɴᴇʀ ᴀɴᴅ + ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ.

🤖 ᴍʏ ɴᴀᴍᴇ: {}

📝 ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>𝕻𝖞𝖙𝖍𝖔𝖓3</a>

📚 ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org>𝕻𝖗𝖔𝖌𝖗𝖆𝖒</a>

🧑🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/itzz_me_alexxa>𝓐𝖑𝖊𝖝𝖝𝖆</a>

👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ: <a href=https://t.me/+eBzYtdaY7Bc2ZDVl>𝕿𝕹 𝕾𝖚𝖕𝖕𝖔𝖗𝖙</a>

📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ: <a href=https://t.me/tn_botz>𝕿𝕹 𝖀𝖕𝖉𝖆𝖙𝖊𝖘</a></b>
""")


Print("Bot Was Started") 

TnBotz.run() 
