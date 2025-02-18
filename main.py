import telebot
from telebot import types

bot = telebot.Telebot('7653029123:AAGZT26o00FphPZloCohvv-QI5-jFKIMBH4')

@bot.messsage_handler(command=['quiz'])
def qustion(message):
     markup = types.InlineKeybordMarkup(row_width=2)

     iron = types.InlineKeybordButton('1 kilo of iron',callback_data=''answeer_text1)
     catton = types.InlineKeybordButton('1 kilo of iron',callback_data=''answeer_text1)
     same = types.InlineKeybordButton('1 kilo of iron',callback_data=''answeer_text1)
     no_answer = types.InlineKeybordButton('1 kilo of iron',callback_data=''answeer_text1)


     markup.add(iron,catton,same,no_answer)
     
     bot.send_messahe(message.chat.id,'what is lighter?', relay_markup=markup)

@bot.callback_query_handlers(func=lambda call:true)
def answer(callback):
     if callback.message:
          if callback.data == 'answer_same':
               bot.send_message(callback.message.chat.id,'congroulation')
          else:
               bot.send_message(callback.message.chat.id,'think again')

bto.polling()
