import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = telebot.types.KeyboardButton("🛏️ Surilarni rasm va narxlari bilan ko‘rish")
    markup.add(btn)
    bot.send_message(message.chat.id, "Xush kelibsiz! Quyidagi tugmani bosing:", reply_markup=markup)

bot.polling()
