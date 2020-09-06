import json
import random
import events

from datetime import datetime

from telegram.ext import Updater, MessageHandler, CommandHandler ,Filters
from telegram import Chat


with open('token.json', 'r') as token_file:
    token_dict = json.load(token_file)

odds = 0.01
numberOfButterGifs = 4

noah_chat_id = 186885633
zarro_chat_id = -426537114

actions = ["Miau", "Butter", "Fueter"]

updater = Updater(token=token_dict["token"])
dispatcher = updater.dispatcher

def message_handler(bot, update):
    # check if it is in a group chat
    if update.message.chat.type == Chat.GROUP or update.message.chat.type == Chat.SUPERGROUP:
        print(update.message.chat_id)
        # check if Gandalf should say something
        if random.random() < odds:
            action = random.choice(actions)
            if action == "Miau":
                print("miau")
                bot.send_message(chat_id=update.message.chat_id, text="Miau!")
            if action == "Butter":
                print("butter")
                picNumber = random.randint(0,numberOfButterGifs-1)
                fileName = 'gifs/butter/'+str(picNumber)+'.gif'
                print(fileName)
                bot.send_animation(chat_id=update.message.chat_id, animation=open(fileName, 'rb'))
            if action == "Fueter":
                print("fueter")
                bot.send_message(chat_id=update.message.chat_id, text="Ich wött Fueter!")

    else:
        print(update.message.chat_id)
        bot.send_message(chat_id=update.message.chat_id, text="I wött nur in Gruppechats chatte")

def say(bot, update):
    if update.message.chat_id == noah_chat_id:
        text = update.message.text.replace("/say ", "")
        print("Gonna tell: " + text)
        bot.send_message(chat_id=zarro_chat_id, text=text)

    else:
        bot.send_message(chat_id=update.message.chat_id, text="Du hesch mir gar nüt zsege")


def send_poll(arg):
    now = datetime.now()
    todays_date = now.strftime("%-d. %B")
    new_poll = updater.bot.send_poll(chat_id=zarro_chat_id, question="Sinder am Fritig zum Znacht do? ("+todays_date+")", options=["Jo", "Nei", "Weiss nonig"], is_anonymous=False)
    updater.bot.pin_chat_message(chat_id=zarro_chat_id,message_id=new_poll.message_id)

dispatcher.add_handler(CommandHandler('say', say))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

updater.start_polling()

reminder_Th = events.TimedEvent(3, 16, 0, send_poll, "Th")

while True:
    reminder_Th.wait()