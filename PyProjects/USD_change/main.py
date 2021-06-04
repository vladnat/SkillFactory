import telebot
from token_ import TOKEN
from extensions import values, ConvertExeptions
      
   
bot = telebot.AsyncTeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '''Привет!
    Напиши /values, чтобы узнать какие валюты есть в наличии.''')

@bot.message_handler(commands=['values'])
def values_(message: telebot.types.Message):
    text = 'Доступные валюты:\n'
    text += '\n'.join(f'{i + 1}. {key}' for i, key in enumerate(values.keys()))
    bot.reply_to(message, text)  
    bot.reply_to(message, '''Напиши  валюту, которую хочешь обменять, 
    валюту, на которую хочешь обменять,
    и сколько - например: usd rub 200''')

# print(values)
@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        arr = message.text.split(' ')
        
        if len(arr) != 3:
            raise ConvertExeptions('Неверное количество параметров')
        base, quote, amount = arr
        
    except ConvertExeptions as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    else:    
        text = f'{round((values[base.upper()] / values[quote.upper()]) * float(amount), 2)} {quote}'
        bot.send_message(message.chat.id, text)
    # print(*arr)
bot.polling()