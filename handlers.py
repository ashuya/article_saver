import config
import queries
import logging
from googlesearch import search
import telegram
from telegram import (
	InlineQueryResultArticle,
	InputTextMessageContent,
	InlineKeyboardButton,
	InlineKeyboardMarkup,
)
from telegram.ext import (
	CommandHandler,
	MessageHandler,
	Filters,
)

logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
	level=logging.INFO)

logger = logging.getLogger()

def start(update, context):
	queries.sign_up_user(update.message.from_user.id)
	help_function(update, context)

def help_function(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['help'])

def change_bot_lang(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])

def change_article_lang(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])

def find(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])

def save(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])

def list_categories(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])

def list_articles(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])

def show_article(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])

def rename_article(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])

def rename_category(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])

def delete_article(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])

def delete_category(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])

def unknown_command(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['unknown'])

handlers = [
	CommandHandler('start', start),
	CommandHandler('help', help_function),
	CommandHandler('botlang', change_bot_lang),
	CommandHandler('lang', change_article_lang),
	CommandHandler('find', find),
	CommandHandler('save', save),
	CommandHandler('listcat', list_categories),
	CommandHandler('listart', list_articles),
	CommandHandler('showart', show_article),
	CommandHandler('renameart', rename_article),
	CommandHandler('renamecat', rename_category),
	CommandHandler('deleteart', delete_article),
	CommandHandler('deletecat', delete_category),
	MessageHandler(Filters.command, unknown_command),
]