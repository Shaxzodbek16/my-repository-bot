from config import BOT_API
from telebot import TeleBot, types

bot = TeleBot(token=BOT_API)


@bot.message_handler(commands=['start'])
def start(message: types.Message) -> None:
	bot.send_message(message.from_user.id, "Assalomu alaykum, Shaxzodbekning botiga xush kelibsiz!")


bot.polling()

