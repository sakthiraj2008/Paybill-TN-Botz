from pyrogram import Client, filters
from pyrogram.types import InlineKeybordMarkup, InlineKeybordButton

API_ID = "11472991"
API_HASH = "c78c50d54baf2173e8b3f75c359c0c72"
BOT_TOKEN = "7653029123:AAGZT26o00FphPZloCohvv-QI5-jFKIMBH4"

TnBotz = Cilent(
     name="PayBill_UPI_Bot", 
     api_id=API_ID, 
     api_hash=API_HASH, 
     bot_token=BOT_TOKEN
) 


START_BUTTONS = [[
  InlineKeybordButtons("Update Channel",url="https://t.me/tn_botz")
]]



@TnBotz.on_message(filters.command("start")) 
async def start_cmd(client, message):
     await meaasge.replay_text(
          text=="you have to join my channel to use me",
          replay_markup=InlineKeybordMarkup(START_BUTTONS)
     )
Print("Bot Was Started") 

TnBotz.run() 
