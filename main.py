import telebot 

token = 'token from @BotFather' 
bot = telebot.TeleBot(token) 

@bot.message_handler(commans=['start']) 
def main(message): 
   bot.send_document(message.chat.id, open('file.zip', 'rb')) 
bot.polling(none_stop = True) 
