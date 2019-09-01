from telegram import Bot, Update
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler

from bot.config import TG_TOKEN, TG_API_URL


def start_bot(bot: Bot, update: Update):
	bot.send_message(
		chat_id=update.message.chat_id,
		text="Hi! Send me smth you want!"
	)


def do_echo(bot: Bot, update: Update):
	text = update.message.text
	bot.send_message(
		chat_id=update.message.chat_id,
		text=text,
	)


def main():
	bot = Bot(
		token=TG_TOKEN,base_url=TG_API_URL
	)
	updater = Updater(
		bot=bot
	)

	start_handler = CommandHandler("start", start_bot)
	message_handler = MessageHandler(Filters.text, do_echo)
	updater.dispatcher.add_handler(start_handler)
	updater.dispatcher.add_handler(message_handler)

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()
