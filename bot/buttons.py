from telebot import types

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

main_keyboard.add(shaxzodbek, people, wish, study, family, friend, game, love)
