import json
import random

from telegram.ext import Updater, MessageHandler, Filters

with open('token.json', 'r') as token_file:
    token_dict = json.load(token_file)


updater = Updater(token=token_dict["token"])
dispatcher = updater.dispatcher

CalvinQuote = ["Uuufhocke!", "Ueloh!", "Wuuuah, wele Sauhund heten den do ieghebet?!","Aaaaaagiiii"]

def message_handler(bot, update):
    message = update.message.text.lower().split()
    if "lano" in message:
        bot.send_message(chat_id=update.message.chat_id, text="Was für ein schöner Name!")
    if "gnigget" in message or "gnighet" in message:
        bot.send_photo(chat_id=update.message.chat_id, photo=open('photos/gnighet.png', 'rb'))
    if "fisch" in message:
        bot.send_message(chat_id=update.message.chat_id, text="Auf den Tisch kommt heut ein Fisch, so saftig süüüüüüüüüüüüss")
    if "calvin" in message:
         bot.send_message(chat_id=update.message.chat_id, text=CalvinQuote[random.randrange(0, len(CalvinQuote), 1)])
    if "scio" in message:
        bot.send_sticker(chat_id=update.message.chat_id, sticker=open('photos/scio_scooter.gif', 'rb'))
        bot.send_message(chat_id=update.message.chat_id, text="Do isch de grüsig cheib")
    if "nutella" in message:
        bot.send_poll(chat_id=update.message.chat_id, question="Wird Nutella mit oder ohni Butter gesse?", options=["Wuah, wilsch mi vegifte?", "Sicher mit, ihr Barbare!"])
    print(update.message.text)


dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
updater.start_polling()