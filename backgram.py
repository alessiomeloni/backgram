import time
import telepot
import subprocess
from telepot.loop import MessageLoop

# ####BOT SETTINGS#####
TOKEN = ""
bot = telepot.Bot(TOKEN)
confirm = "Done"
# ####BOT SETTINGS#####


# ####FUNCTION#####
def sender(msgcontent, chatid):
    response = subprocess.run(
        msgcontent, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    data = response.stdout + response.stderr
    data = str(data, "UTF-8")
    if data == "":
        bot.sendMessage(chatid, confirm)
    else:
        bot.sendMessage(chatid, "Console output:\n" + data)


# ####FUNCTION#####


# ####Master Function#####
def engine(msg):
    contentType, chatType, chatId = telepot.glance(msg)
    msgcontent = msg["text"]

    if contentType == "text" and msgcontent != "/start":
        print(time.strftime("[%x][%X] - Received an Input"))
        sender(msgcontent, chatId)


# ####Master Function#####

# ####MessageLoop#####
MessageLoop(bot, engine).run_as_thread()
print(time.strftime("[%x][%X] - Engine Online"))
while True:
    time.sleep(10)
# ####MessageLoop#####
