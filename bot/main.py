from config import BOT_API
from telebot import TeleBot, types
import buttons
import information

bot = TeleBot(token=BOT_API)


@bot.message_handler(commands=['start'])
def buttons_show(message: types.Message) -> None:
	text: str = "Quyidagilardan birini tanlang 👇"
	bot.send_message(message.from_user.id, text=text, reply_markup=buttons.main_keyboard)


@bot.message_handler()
def main_keyboard(message: types.Message) -> None:
	match message.text:
		case "Shaxzodbek👤":
			bot.send_message(message.from_user.id, text=information.shaxzodbek(0))
		case "People":
			bot.send_message(message.from_user.id, text=information.people(0)["people"][0]["first_name"])
		case "Wish✨":
			bot.send_message(message.from_user.id, text=information.wish(0)['title'])
		case "Study👨‍🎓":
			bot.send_message(message.from_user.id, text=information.shaxzodbek(0, "study"))
		case "Family":
			bot.send_message(message.from_user.id, text=information.shaxzodbek(0, "family"))
		case "Friend":
			bot.send_message(message.from_user.id, text=information.shaxzodbek(0, "friend"))
		case "Game":
			bot.send_message(message.from_user.id, text=information.shaxzodbek(0, "game"))
		case "Love💕":
			bot.send_message(message.from_user.id, text=information.shaxzodbek(0, "love"))


bot.polling()
