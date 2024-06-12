from config import BOT_API
from telebot import TeleBot, types
import buttons
import information

bot = TeleBot(token=BOT_API)


# @bot.message_handler(commands=['start'])
# def start(message: types.Message) -> None:
# 	text: str = "Telefon raqamingizni kiriting"
# 	bot.send_message(message.chat.id, text=text, reply_markup=buttons.information_container)
#
#
# @bot.message_handler(content_types=['contact'])
# def contact(message: types.Message) -> None:
# 	text: str = f"Salom, {message.contact.first_name}, {message.contact.last_name}"
# 	bot.send_message(message.from_user.id, text=text)


@bot.message_handler(commands=['start'])
def buttons_show(message: types.Message) -> None:
	text: str = ("Quyidagilardan birini tanlang 👇")
	bot.send_message(message.from_user.id, text=text, reply_markup=buttons.main_keyboard)


@bot.message_handler()
def main_keyboard(message: types.Message) -> None:
	match message.text:
		case "Shaxzodbek👤":
			bot.send_message(message.from_user.id, text=information.shaxzodbek)
		case "People":
			bot.send_message(message.from_user.id, text=information.people)
		case "Wish✨":
			bot.send_message(message.from_user.id, text=information.wish)
		case "Study👨‍🎓":
			bot.send_message(message.from_user.id, text=information.study)
		case "Family":
			bot.send_message(message.from_user.id, text=information.family)
		case "Friend":
			bot.send_message(message.from_user.id, text=information.friend)
		case "Game":
			bot.send_message(message.from_user.id, text=information.game)
		case "Love💕":
			bot.send_message(message.from_user.id, text=information.love)
		case "Copilot":
			bot.send_message(message.from_user.id, text=information.Copilot)
		case "Gemini":
			bot.send_message(message.from_user.id, text=information.Gemini)
		case "ChatGPT":
			bot.send_message(message.from_user.id, text=information.ChatGPT)
		case _:
			bot.send_message(message.from_user.id, text=information.default)


bot.polling()
