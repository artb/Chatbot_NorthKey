import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("514870778:AAEX6CGILjGita7qxAVQcKVPinXhw-Dt8O8")
bot = Chatbot("NorthKey_bot")

def recebendoMsg(msg):
	frase = bot.escuta(frase=msg['text'])
	resp = bot.pensa(frase)
	bot.fala(resp)
	tipoMsg, tipoChat, chatID = telepot.glance(msg)
	telegram.sendMessage(chatID,resp)

telegram.message_loop(recebendoMsg)

while True:
	pass