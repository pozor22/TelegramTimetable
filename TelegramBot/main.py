import telebot
from telebot import types
import psycopg2
import datetime
from datetime import date, time, datetime

bot = telebot.TeleBot("5918045561:AAF8hzcnyXlEeEuHu7r77Yb6Yqp0kve1nu8")

conn = psycopg2.connect(database='timetable_2203', user='postgres', password='1234', host='127.0.0.1', port='5432')
cursor = conn.cursor()
# cursor.execute("SELECT * FROM timetable")
# records = list(cursor.fetchall())
# bot.send_message(message.chat.id, f'{records[0][0], records[0][1], records[0][2]}')

#щас 13 неделя неч\тная

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Понедельник')
    item2 = types.KeyboardButton('Вторник')
    item3 = types.KeyboardButton('Среда')
    item4 = types.KeyboardButton('Четверг')
    item5 = types.KeyboardButton('Пятница')
    item6 = types.KeyboardButton('Расписание на текущую неделю')
    item7 = types.KeyboardButton('Расписание на следующую неделю')
    item8 = types.KeyboardButton('/help')
    keyboard.add(item1, item2, item3, item4, item5, item6, item7, item8)
    bot.send_message(message.chat.id, 'я бот, который показывает расписание для группы БФИ2203', reply_markup=keyboard)

@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Я бот с расписанием для группы БФИ2203 \r\nя умею: '
                                      '\r\nкнопка "понедельник" - расписание на понедельник'
                                      '\r\nкнопка "вторник" - расписание на вторник'
                                      '\r\nкнопка "среда" - расписание на среду'
                                      '\r\nкнопка "четверг" - расписание на четверг'
                                      '\r\nкнопка "пятница" - расписание на пятницу'
                                      '\r\nкнопка "расписание на текущую неделю" - расписание на текущую неделю'
                                      '\r\nкнопка "расписание на следующую неделю" - расписание на следующую неделю'
                                      '\r\n/mtuci - ссылка на сайт мтуси'
                                      '\r\n/week - покажу какая щас неделя')

@bot.message_handler(commands=['week'])
def week(message):
    day = int(datetime.today().isocalendar().week)
    if day % 2 == 1:
        bot.send_message(message.chat.id, f'Сейчас нечетная неделя')
    else:
        bot.send_message(message.chat.id, f'Сейчас четная неделя')

# text
@bot.message_handler()
def get_user_text(message):
    day = int(datetime.today().isocalendar().week)
    if day % 2 == 1:
        if message.text == 'Понедельник':
            cursor.execute("SELECT * FROM mon1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Понедельник '
                                            f'\r\n1. {par1} '
                                            f'\r\n2. {par2} '
                                            f'\r\n3. {par3} '
                                            f'\r\n4. {par4} '
                                            f'\r\n5. {par5}')
        elif message.text == 'Вторник':
            cursor.execute("SELECT * FROM tues1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Вторник '
                                          f'\r\n1. {par1} '
                                          f'\r\n2. {par2} '
                                          f'\r\n3. {par3} '
                                          f'\r\n4. {par4} '
                                          f'\r\n5. {par5}')
        elif message.text == 'Среда':
            cursor.execute("SELECT * FROM wed1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Среда '
                                          f'\r\n1. {par1} '
                                          f'\r\n2. {par2} '
                                          f'\r\n3. {par3} '
                                          f'\r\n4. {par4} '
                                          f'\r\n5. {par5}')
        elif message.text == 'Четверг':
            cursor.execute("SELECT * FROM thu1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Четверг '
                                            f'\r\n1. {par1} '
                                            f'\r\n2. {par2} '
                                            f'\r\n3. {par3} '
                                            f'\r\n4. {par4} '
                                            f'\r\n5. {par5}')
        elif message.text == 'Пятница':
            cursor.execute("SELECT * FROM fri1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Пятница '
                                            f'\r\n1. {par1} '
                                            f'\r\n2. {par2} '
                                            f'\r\n3. {par3} '
                                            f'\r\n4. {par4} '
                                            f'\r\n5. {par5}')
        elif message.text == 'Расписание на текущую неделю':
            cursor.execute("SELECT * FROM mon1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Понедельник '
                                                  f'\r\n1. {par1} '
                                                  f'\r\n2. {par2} '
                                                  f'\r\n3. {par3} '
                                                  f'\r\n4. {par4} '
                                                  f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM tues1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Вторник '
                                                  f'\r\n1. {par1} '
                                                  f'\r\n2. {par2} '
                                                  f'\r\n3. {par3} '
                                                  f'\r\n4. {par4} '
                                                  f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM wed1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Среда '
                                                  f'\r\n1. {par1} '
                                                  f'\r\n2. {par2} '
                                                  f'\r\n3. {par3} '
                                                  f'\r\n4. {par4} '
                                                  f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM thu1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Четверг '
                                                  f'\r\n1. {par1} '
                                                  f'\r\n2. {par2} '
                                                  f'\r\n3. {par3} '
                                                  f'\r\n4. {par4} '
                                                  f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM fri1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Пятница '
                                                  f'\r\n1. {par1} '
                                                  f'\r\n2. {par2} '
                                                  f'\r\n3. {par3} '
                                                  f'\r\n4. {par4} '
                                                  f'\r\n5. {par5}')
        elif message.text == 'Расписание на следующую неделю':
            cursor.execute("SELECT * FROM mon2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Понедельник '
                                                  f'\r\n1. {par1} '
                                                  f'\r\n2. {par2} '
                                                  f'\r\n3. {par3} '
                                                  f'\r\n4. {par4} '
                                                  f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM tues2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Вторник '
                                                  f'\r\n1. {par1} '
                                                  f'\r\n2. {par2} '
                                                  f'\r\n3. {par3} '
                                                  f'\r\n4. {par4} '
                                                  f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM wed2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Среда '
                                                  f'\r\n1. {par1} '
                                                  f'\r\n2. {par2} '
                                                  f'\r\n3. {par3} '
                                                  f'\r\n4. {par4} '
                                                  f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM thu2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Четверг '
                                                  f'\r\n1. {par1} '
                                                  f'\r\n2. {par2} '
                                                  f'\r\n3. {par3} '
                                                  f'\r\n4. {par4} '
                                                  f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM fri2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Пятница '
                                                  f'\r\n1. {par1} '
                                                  f'\r\n2. {par2} '
                                                  f'\r\n3. {par3} '
                                                  f'\r\n4. {par4} '
                                                  f'\r\n5. {par5}')
        else:
            bot.send_message(message.chat.id, 'Извините, я Вас не понял')
    elif day % 2 == 0:
        if message.text == 'Понедельник':
            cursor.execute("SELECT * FROM mon2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Понедельник '
                                            f'\r\n1. {par1} '
                                            f'\r\n2. {par2} '
                                            f'\r\n3. {par3} '
                                            f'\r\n4. {par4} '
                                            f'\r\n5. {par5}')
        elif message.text == 'Вторник':
            cursor.execute("SELECT * FROM tues2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Вторник '
                                          f'\r\n1. {par1} '
                                          f'\r\n2. {par2} '
                                          f'\r\n3. {par3} '
                                          f'\r\n4. {par4} '
                                          f'\r\n5. {par5}')
        elif message.text == 'Среда':
            cursor.execute("SELECT * FROM wed2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Среда '
                                          f'\r\n1. {par1} '
                                          f'\r\n2. {par2} '
                                          f'\r\n3. {par3} '
                                          f'\r\n4. {par4} '
                                          f'\r\n5. {par5}')
        elif message.text == 'Четверг':
            cursor.execute("SELECT * FROM thu2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Четверг '
                                            f'\r\n1. {par1} '
                                            f'\r\n2. {par2} '
                                            f'\r\n3. {par3} '
                                            f'\r\n4. {par4} '
                                            f'\r\n5. {par5}')
        elif message.text == 'Пятница':
            cursor.execute("SELECT * FROM fri2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Пятница '
                                            f'\r\n1. {par1} '
                                            f'\r\n2. {par2} '
                                            f'\r\n3. {par3} '
                                            f'\r\n4. {par4} '
                                            f'\r\n5. {par5}')

        elif message.text == 'Расписание на следующую неделю':
            cursor.execute("SELECT * FROM mon1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Понедельник '
                                              f'\r\n1. {par1} '
                                              f'\r\n2. {par2} '
                                              f'\r\n3. {par3} '
                                              f'\r\n4. {par4} '
                                              f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM tues1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Вторник '
                                              f'\r\n1. {par1} '
                                              f'\r\n2. {par2} '
                                              f'\r\n3. {par3} '
                                              f'\r\n4. {par4} '
                                              f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM wed1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Среда '
                                              f'\r\n1. {par1} '
                                              f'\r\n2. {par2} '
                                              f'\r\n3. {par3} '
                                              f'\r\n4. {par4} '
                                              f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM thu1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Четверг '
                                              f'\r\n1. {par1} '
                                              f'\r\n2. {par2} '
                                              f'\r\n3. {par3} '
                                              f'\r\n4. {par4} '
                                              f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM fri1")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Пятница '
                                              f'\r\n1. {par1} '
                                              f'\r\n2. {par2} '
                                              f'\r\n3. {par3} '
                                              f'\r\n4. {par4} '
                                              f'\r\n5. {par5}')
        elif message.text == 'Расписание на текущую неделю':
            cursor.execute("SELECT * FROM mon2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Понедельник '
                                              f'\r\n1. {par1} '
                                              f'\r\n2. {par2} '
                                              f'\r\n3. {par3} '
                                              f'\r\n4. {par4} '
                                              f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM tues2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Вторник '
                                              f'\r\n1. {par1} '
                                              f'\r\n2. {par2} '
                                              f'\r\n3. {par3} '
                                              f'\r\n4. {par4} '
                                              f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM wed2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Среда '
                                              f'\r\n1. {par1} '
                                              f'\r\n2. {par2} '
                                              f'\r\n3. {par3} '
                                              f'\r\n4. {par4} '
                                              f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM thu2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Четверг '
                                              f'\r\n1. {par1} '
                                              f'\r\n2. {par2} '
                                              f'\r\n3. {par3} '
                                              f'\r\n4. {par4} '
                                              f'\r\n5. {par5}')

            cursor.execute("SELECT * FROM fri2")
            records = list(cursor.fetchall())
            par1 = records[0][2] + ' ' + records[0][0] + '\r\n' + records[0][1] + ' ' + records[0][3] + '\r\n'
            par2 = records[1][2] + ' ' + records[1][0] + '\r\n' + records[1][1] + ' ' + records[1][3] + '\r\n'
            par3 = records[2][2] + ' ' + records[2][0] + '\r\n' + records[2][1] + ' ' + records[2][3] + '\r\n'
            par4 = records[3][2] + ' ' + records[3][0] + '\r\n' + records[3][1] + ' ' + records[3][3] + '\r\n'
            par5 = records[4][2] + ' ' + records[4][0] + '\r\n' + records[4][1] + ' ' + records[4][3] + '\r\n'
            bot.send_message(message.chat.id, f'Пятница '
                                              f'\r\n1. {par1} '
                                              f'\r\n2. {par2} '
                                              f'\r\n3. {par3} '
                                              f'\r\n4. {par4} '
                                              f'\r\n5. {par5}')
        else:
            bot.send_message(message.chat.id, 'Извините, я Вас не понял')


##

if __name__ == '__main__':
    bot.polling()