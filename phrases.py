phrases = dict()
phrases['ru'] = dict()
phrases['en'] = dict()

#Русский
phrases['ru']['help'] = """
Я ищу и сохраняю актуальные статьи по интересующей вас теме.
С помощью этих команд можно

/botlang - выбрать язык, на котором я буду с вами общаться
/lang - выбрать язык искомых статей
/find - найти статьи
/save - сохранить статью(можете сохранить любую ссылку)

/listcat - посмотреть список ваших категорий
/listart - посмотреть список статей по одной из категорий
/showart - посмотреть статью

/renameart - переименовать статью(они сохраняются по выбранным вами названиям)
/renamecat - переименовать категорию(статьи сохраняются по выбранным вами категориям)
/deleteart - удалить статью
/deletecat - удалить категорию(все статьи из этой категории тоже удаляются)

Бот находится в разработке, вопросы можно задавать разработчику: @desentcare
"""

phrases['ru']['bot_lang_choise'] = "Выберите язык бота:"
phrases['ru']['bot_lang_choise_done'] = "Теперь я говорю на русском!"

phrases['ru']['news_query'] = "Введите поисковой запроc\nНапишите /cancel чтобы ничего не искать"
phrases['ru']['news_query_canceled'] = "Поик остановлен!"
phrases['ru']['news_query_searching'] = "Ищем..."
phrases['ru']['news_query_article_show'] = "Статья №"

phrases['ru']['save_article'] = "Сохраняю статью\n"
phrases['ru']['save_article_category'] = "В какую категорию сохранить вашу статью?\n\
Напишите номер или имя категории из списка, или новую категорию\nВаши категории:\n"
phrases['ru']['save_article_name'] = "Под каким именем сохранить статью?"
phrases['ru']['article_name_same'] = \
"Имя занято. Сначала удалите или переименуйте статью с этим именем"
phrases['ru']['save_article_complete'] = "Статья сохранена!"
phrases['ru']['save_article_cancel'] = "Сохранение стати остановлено!"

phrases['ru']['rename_article_choose_category'] = \
"Из какой категории вы хотите переименовать статью?\n\
Напишите номер или имя категории из списка\n\
(/cancel для отмены)\n\
Ваши категории:\n"
phrases['ru']['rename_article'] = "Какую статью вы хотите переименовать?\n\
Напишите номер или имя статьи из списка\n\
Ваши статьи:\n"
phrases['ru']['rename_article_input'] = "Новое имя для статьи:"
phrases['ru']['rename_article_cancel'] = "Переименование статьи отменено"
phrases['ru']['rename_article_complite'] = "Статья переименована!"

phrases['ru']['rename_category'] = "Какую категорию вы хотите переименовать?\n\
Напишите номер или имя категории из списка\n\
(/cancel для отмены)\n\
Ваши категории:\n"
phrases['ru']['rename_category_input'] = "Новое имя для категории:"
phrases['ru']['rename_category_cancel'] = "Переименование категории отменено"
phrases['ru']['rename_category_complite'] = "Категория переименована!"

phrases['ru']['list_categories'] = "Ваши категории:\n"
phrases['ru']['list_articles'] = "Ваши статьи в категории:\n"
phrases['ru']['show_article_choose_category'] = "Из какой категории взять статью?\n\
Напишите номер или имя категории из списка\n\
(/cancel для отмены)\n\
Ваши категории:\n"
phrases['ru']['show_article_choose_article'] = "Какую статью показать?\n\
Напишите номер или имя статьи из списка\n\
Ваши статьи:\n"


phrases['ru']['delete_category'] = "Напишите имя или номер категории, которую хотите удалить\n\
(Все статьи из этой категории тоже будут удалены. для отмены напишите /cancel)\n\
Ваши категории:\n"
phrases['ru']['delete_category_cancel'] = "Не удаляю категорию"
phrases['ru']['delete_category_complete'] = "Категория удалена"

phrases['ru']['delete_article_choose_category'] = "Из какой категории удалить статью?\n\
Напишите номер или имя категории из списка\n\
(/cancel для отмены)\n\
Ваши категории:\n"
phrases['ru']['delete_article'] = "Какую статью удалить?\n\
Напишите номер или имя статьи из списка\n\
Ваши статьи:\n"
phrases['ru']['delete_article_cancel'] = "Удаление статьи отменено"
phrases['ru']['delete_article_complite'] = "Статья удалена!"

phrases['ru']['indev'] = "Команда разрабатывается"
phrases['ru']['unknown'] = "Команда не распознана"

#English

phrases['en']['help'] = """
I can find and save articles on your topic.
With this commands you can

/botlang - change bot language
/lang - change article language
/find - search for articles
/save - save article(you can save any link)

/listcat - show list of categories
/listart - show list of articles in category
/showart - show one article

/renameart - change nickname for article
/renamecat - change nickname for category
/deleteart - delete article
/deletecat - delete category(also deletes all articles in this category)

Bot is under development, send your questions to @desentcare
"""

phrases['en']['bot_lang_choise'] = "Choose bot language:"
phrases['en']['bot_lang_choise_done'] = "Now I speak english!"

phrases['en']['news_query'] = "Input search query\n/cancel to stop search"
phrases['en']['news_query_canceled'] = "Search canceled!"
phrases['en']['news_query_searching'] = "Searching..."
phrases['en']['news_query_article_show'] = "Article №"

phrases['en']['save_article'] = "Saving article\n"
phrases['en']['save_article_category'] = "In which category I must save article?\n\
Input number or name of category from the list or new category\n\
Your categories:\n"
phrases['en']['save_article_name'] = "Input name of your article to save"
phrases['en']['article_name_same'] = "This name is taken. Delete or rename old article to save new with this name"
phrases['en']['save_article_complete'] = "Article was saved!"
phrases['en']['save_article_cancel'] = "Article saving was stopped"

phrases['en']['rename_article_choose_category'] = "From which category do you want to rename your article?\n\
Input number or name of category from the list\n\
(/cancel to cancel)\n\
Your categories:\n"
phrases['en']['rename_article'] = "What article do you want to rename?\n\
Input number or name of article from the list\n\
Your articles:\n"
phrases['en']['rename_article_input'] = "Input new name for this article:"
phrases['en']['rename_article_cancel'] = "Renaming canceled"
phrases['en']['rename_article_complite'] = "Article was renamed!"

phrases['en']['rename_category'] = "What category do you want to rename?\n\
Input number or name of category from the list\n\
(/cancel to cancel)\n\
Your categories:\n"
phrases['en']['rename_category_input'] = "Input new name for this category:"
phrases['en']['rename_category_cancel'] = "Renaming canceled"
phrases['en']['rename_category_complite'] = "Category was renamed!"

phrases['en']['list_categories'] = "Your categories:\n"
phrases['en']['list_articles'] = "Your articles in this category:\n"
phrases['en']['show_article_choose_category'] = "From which category to show article?\n\
Input number or name of category from the list\n\
(/cancel to cancel)\n\
Your categories:\n"
phrases['en']['show_article_choose_article'] = "What article to show?\n\
Input number or name of article from the list\n\
Your articles:\n"


phrases['en']['delete_category'] = "Input number or name of category to delete\n\
(All articles in this category would be deleted. /cancel to cancel)\n\
Your categories:\n"
phrases['en']['delete_category_cancel'] = "Deleting canceled"
phrases['en']['delete_category_complete'] = "Category was deleted"

phrases['en']['delete_article_choose_category'] = "From which category to delete article?\n\
Input number or name of category from the list\n\
(/cancel to cancel)\n\
Your categories:\n"
phrases['en']['delete_article'] = "Which article to delete?\n\
Input number or name of article from the list\n\
Your articles:\n"
phrases['en']['delete_article_cancel'] = "Deleting canceled"
phrases['en']['delete_article_complite'] = "Article was deleted!"

phrases['en']['indev'] = "Command in development"
phrases['en']['unknown'] = "Unknown command"