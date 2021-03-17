import sqlite3
import config
import phrases
import logging

logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
	level=logging.INFO)

logger = logging.getLogger()

def sign_up_user(user_id: str):
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("SELECT * FROM user_data WHERE user_id=?", (user_id,))
	results = c.fetchall()
	if not results:
		c.execute("""INSERT INTO user_data (user_id) VALUES(?)""",
		 (user_id,))
		logger.info("New user %s", user_id)
		con.commit()
	con.close()

def get_phrases(user_id: str) -> dict:
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("SELECT bot_lang FROM user_data WHERE user_id=?", (user_id,))
	result = c.fetchone()
	if not result:
		sign_up_user(user_id)
	result = ('ru',)
	return phrases.phrases[result[0]]

def init_db():
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("""CREATE TABLE IF NOT EXISTS 'user_data'(
		user_id str PRIMARY KEY,
		bot_lang str NOT NULL DEFAULT 'ru',
		lang str NOT NULL DEFAULT 'ru',
		role str NOT NULL DEFAULT 'user'
		);""")
	c.execute("""CREATE TABLE IF NOT EXISTS articles(
		user_id str,
		category str NOT NULL,
		name str NOT NULL,
		link str
		);""")
	con.commit()
	con.close()

def change_bot_lang(user_id: str, lang: str):
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("""UPDATE user_data
	SET bot_lang = ?
	WHERE user_id = ?""", (lang, user_id))
	con.commit()
	con.close()

def change_article_lang(user_id: str, lang: str):
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("""UPDATE user_data
	SET lang = ?
	WHERE user_id = ?""", (lang, user_id))
	con.commit()
	con.close()

def add_article(user_id: str, category: str, name: str, link: str):
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("""INSERT INTO articles(user_id, category, name, link)
	VALUES (?,?,?,?)""", (user_id, category, name, link))
	logger.info("%s added %s article to %s category", user_id, name, category)
	con.commit()
	con.close()

def get_article(user_id: str, category: str, name: str) -> str:
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("""SELECT link FROM articles WHERE user_id=? AND category = ? AND name=?""",
	(user_id, category, name))
	logger.info("%s got %s article from %s category", user_id, name, category)
	result = c.fetchone()
	con.close()
	return result[0]

def get_categories(user_id: str) -> list:
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("""SELECT DISTINCT category FROM articles WHERE user_id=?""", (user_id,))
	result = c.fetchall()
	con.close()
	return [e[0] for e in result]

def get_articles(user_id: str, category: str) -> list:
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("""SELECT name FROM articles WHERE user_id=? AND category=?""",
	(user_id,category))
	result = c.fetchall()
	con.close()
	return [e[0] for e in result]

def rename_article(user_id:str,category:str, name: str, new_name: str):
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("""UPDATE articles
	SET name = ?
	WHERE user_id = ? AND category = ? AND name = ?""", (new_name, user_id, category, name))
	logger.info("%s renamed %s article to %s", user_id, name, new_name)
	con.commit()
	con.close()

def rename_category(user_id: str, category: str, new_name: str):
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("""UPDATE articles
	SET category = ?
	WHERE user_id = ? AND category = ?""", (new_name, user_id, category))
	logger.info("%s renamed %s category to %s", user_id, category, new_name)
	con.commit()
	con.close()

def delete_article(user_id: str, category: str, name: str):
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("""DELETE FROM articles
	WHERE user_id = ? AND category = ? AND name = ?""", (user_id, category, name))
	logger.info("%s deleted %s article", user_id, article)
	con.commit()
	con.close()

def delete_category(user_id: str, category: str):
	con = sqlite3.connect(config.db_name)
	c = con.cursor()
	c.execute("""DELETE FROM articles
	WHERE user_id = ? AND category = ?""", (user_id, category))
	logger.info("%s deleted %s category", user_id, category)
	con.commit()
	con.close()

def main():
	init_db()

if __name__=="__main__":
	main()
