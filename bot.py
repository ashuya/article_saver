import config
import handlers
import sqlite3
import telegram
from telegram.ext import (
	Updater,
	ConversationHandler,
	MessageFilter,
	MessageHandler,
	CommandHandler,
	Filters,
	CallbackContext,
)

updater = Updater(token=config.TOKEN, use_context=True)
dispatcher = updater.dispatcher

for h in handlers.handlers:
	dispatcher.add_handler(h)

def main():
	updater.start_polling()
	updater.idle()

if __name__=="__main__":
	main()