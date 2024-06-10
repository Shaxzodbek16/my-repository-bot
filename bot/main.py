import os
from telebot import TeleBot, types

bot_token = os.environ.get('BOT_API')
bot = TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def start(message: types.Message) -> None:
	bot.send_message(message.from_user.id, "Assalomu alaykum, Shaxzodbekning botiga xush kelibsiz!")


bot.polling()

