from os import write
from telegram.ext.conversationhandler import ConversationHandler
import config
import queries
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
	CallbackQueryHandler,
)

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
	phrases['bot_lang_choise'], reply_markup = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton('Русский',callback_data='bl;ru'),
				InlineKeyboardButton('English',callback_data='bl;en')
			]
		]
	))

def find(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['news_query'])
	return 1

def find_results(update, context):
	q = update.message.text
	phrases = queries.get_phrases(update.message.from_user.id)
	message = update.message.reply_text(
	text=phrases['news_query_searching'])
	print(q)
	results = []
	for url in search(q, tld='com.ru', lang=queries.get_lang(update.message.from_user.id), stop=6):
		results.append(url)
	if len(results) < 6:
		message.edit_text(phrases['news_query_not_found'])
	choice = 0
	queries.save_results(update.message.from_user.id, results)
	message.edit_text(results[choice],reply_markup = get_article_markup(results,choice))
	return ConversationHandler.END

def get_article_markup(results, choice):
	markup = InlineKeyboardMarkup(
		[
			[InlineKeyboardButton('Сохранить эту статью', callback_data=f's;{choice}')],
		[
			InlineKeyboardButton('(1)' if choice == 0 else '1', callback_data='a;0'),
			InlineKeyboardButton('(2)' if choice == 1 else '2', callback_data='a;1'),
			InlineKeyboardButton('(3)' if choice == 2 else '3', callback_data='a;2'),
		],
		[
			InlineKeyboardButton('(4)' if choice == 3 else '4', callback_data='a;3'),
			InlineKeyboardButton('(5)' if choice == 4 else '5', callback_data='a;4'),
			InlineKeyboardButton('(6)' if choice == 5 else '6', callback_data='a;5')
		]
		]
	)
	return markup

def change_article_button(update,context):
	query = update.callback_query
	query.answer()
	data = query.data.split(';')
	choice = int(data[1])
	results = queries.get_results(update.callback_query.message.chat.id)
	query.edit_message_text(results[choice], reply_markup = get_article_markup(results,choice))

def save_button(update, context):
	query = update.callback_query
	query.answer()
	phrases = queries.get_phrases(query.message.chat.id)
	data = query.data.split(';')
	choice = int(data[1])
	queries.add_article(query.message.chat.id, queries.get_results(query.message.chat.id)[choice])
	categories = queries.get_categories(query.message.chat.id)
	categories = '\n'.join([str(i)+'. '+categories[i] for i in range(len(categories))])
	if not categories:
		categories = phrases['no_categories']
	query.message.reply_text(phrases['save_article_category']+categories)
	return 1

def save_first(update, context):
	categories = queries.get_categories(update.message.from_user.id)
	phrases = queries.get_phrases(update.message.from_user.id)
	answer = update.message.text
	if answer.isnumeric():
		answer = int(answer)
		if len(categories) <= answer or answer < 0:
			categories = '\n'.join([str(i)+'. '+categories[i] for i in range(len(categories))])
			update.message.reply_text(phrases['wrong_category']+categories)
			return 1
		else:
			queries.add_article_cat(update.message.from_user.id, categories[answer])
			update.message.reply_text(phrases['save_article_name'])
			return 2
	queries.add_article_cat(update.message.from_user.id, answer)
	update.message.reply_text(phrases['save_article_name'])
	return 2

def save_second(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	queries.add_article_name(update.message.from_user.id, update.message.text)
	update.message.reply_text(phrases['save_article_complete'])
	return ConversationHandler.END

def list_categories(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	phrases['list_categories']+'\n'.join(queries.get_categories(update.message.from_user.id)))

def list_articles(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	categories = queries.get_categories(update.message.from_user.id)
	text = [] 
	for c in categories:
		articles = queries.get_articles(update.message.from_user.id, c)
		text += [c] + list(map(lambda x: x[0]+': '+x[1], articles))
	update.message.reply_text('\n'.join(text))

def rename_article(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	phrases['rename_article_choose_category']+'\n'.join(queries.get_categories(update.message.from_user.id)))
	return 1

def rename_article_cat(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	return 2

def rename_article_name(update, context):
	return 3

def rename_article_new_name(update, context):
	return ConversationHandler.END

def rename_category(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	return 1

def rename_category_cat(update, context):
	return 2

def rename_category_new_name(update, context):
	return ConversationHandler.END

def delete_article(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])


def delete_article_cat(update, context):
	return 2

def delete_article_name(update, context):
	return ConversationHandler.END

def delete_category(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['indev'])

def delete_category_cat(update, context):
	return ConversationHandler.END


def unknown_command(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['unknown'])

def stop(update, context):
	phrases = queries.get_phrases(update.message.from_user.id)
	queries.cancel_save(update.message.from_user.id)
	update.message.reply_text(
	text=phrases['stop'])
	return ConversationHandler.END

def bot_lang_button(update, context):
	query = update.callback_query
	query.answer()
	data = query.data.split(';')
	queries.change_bot_lang(query.message.chat.id, data[1])
	phrases = queries.get_phrases(query.message.chat.id)
	query.message.reply_text(phrases['bot_lang_choise_done'])

handlers = [
	ConversationHandler(
		entry_points=[CommandHandler('find', find)],
		states={
			1:[MessageHandler(Filters.text & ~Filters.command, find_results)],
		},
		fallbacks=[CommandHandler('cancel', stop)]),
	ConversationHandler(
		entry_points=[CallbackQueryHandler(save_button, pattern='^s;*', pass_user_data=True, pass_chat_data=True)],
		states={
			1:[MessageHandler(Filters.text & ~Filters.command, save_first)],
			2:[MessageHandler(Filters.text & ~Filters.command, save_second)],
		},
		fallbacks=[CommandHandler('cancel', stop)]),

	CommandHandler('start', start),
	CommandHandler('cancel', stop),
	CommandHandler('help', help_function),
	CommandHandler('botlang', change_bot_lang),
	CommandHandler('listcat', list_categories),
	CallbackQueryHandler(change_article_button,pattern='^a;*', pass_user_data=True, pass_chat_data=True),
	CallbackQueryHandler(save_button, pattern='^s;*', pass_user_data=True, pass_chat_data=True),
	CallbackQueryHandler(bot_lang_button, pattern='^bl;*'),
	CommandHandler('listart', list_articles),
	MessageHandler(Filters.command, unknown_command),
]