from telebot import types

#  take info from user
information_container = types.ReplyKeyboardMarkup(resize_keyboard=True)
information_taker = types.KeyboardButton("Share contact", request_contact=True)
information_container.add(information_taker,)


# about database information
main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
shaxzodbek = types.KeyboardButton("Shaxzodbek👤")
people = types.KeyboardButton("People")
wish = types.KeyboardButton("Wish✨")
study = types.KeyboardButton("Study👨‍🎓")
family = types.KeyboardButton("Family")
friend = types.KeyboardButton("Friend")
game = types.KeyboardButton("Game")
love = types.KeyboardButton("Love💕")
copilot = types.KeyboardButton("Copilot")
gemini = types.KeyboardButton("Gemini")
chatGPT = types.KeyboardButton("ChatGPT")

main_keyboard.add(shaxzodbek, people, wish, study, family, friend, game, love, copilot, gemini, chatGPT)
