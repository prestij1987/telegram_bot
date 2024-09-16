from secret import token
import psycopg2
import configparser
import telebot

# create table tg_bot_user(id int primary key);

class MyBot(telebot.TeleBot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__users = {}
        
        self.__conn = self.__connect_to_pg()
        try:
            self.__load_users()
        except:
            print('No users')
    
    def __connect_to_pg(self):
        config = configparser.ConfigParser()
        config.read('C:/Users/Student/AppData/Roaming/postgresql/.pg_service.conf')
        return psycopg2.connect(
            'dbname=%s user=%s' % (
                config.get('tudushka', 'dbname'),
                config.get('tudushka', 'user')
                )
            )

    def add_user(self, msg):
        cursor = self.__conn.cursor()
        cursor.execute(
            'INSERT INTO tg_bot_user(id) VALUES (%s)' % (
                msg.chat.id
            ))
        self.__conn.commit()
        cursor.close()
    
    def __load_users(self):
        'SELECT * from tg_bot_user'
        #cursor.fetchall()