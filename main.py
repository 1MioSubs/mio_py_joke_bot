import requests
import random
import telebot
from bs4 import BeautifulSoup as b
import datetime
from calendar import monthrange

#https://www.anekdot.ru/last/good/
#6193563559:AAHbSdaV5ct0BfLHZze4hOuh7_cmU37HP98
#t.me/miosubs_bot


URL = 'https://www.anekdot.ru/last/good/'
API_KEE = '6193563559:AAHbSdaV5ct0BfLHZze4hOuh7_cmU37HP98'
list_of_jokes = ['1', '2', '3']

def ran_date(a, b):
    return random.randint(a, b)

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

def test(d):
    global list_of_jokes
    list_of_jokes = parser(URL + str(d))
    random.shuffle(list_of_jokes)

def test1():
    global list_of_jokes
    list_of_jokes = parser(URL)
    random.shuffle(list_of_jokes)

test1()

bot = telebot.TeleBot(API_KEE)
@bot.message_handler(commands=['start'])
def hello(message):
    test1()
    bot.send_message(message.chat.id, "Если хотите еще =) \nможно написать (рандом - для рандомного дня) или (новые - это самые свежие за сегодня) или (введите свою дату с 2012-01-01 по сегодня в таком формате (" + str(datetime.date.today()) + ")) и я выберу новую партию шуточек \nПосле чего выбери цифру от 1 до 9:")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Если хотите еще =) \nможно написать (рандом - для рандомного дня) или (новые - это самые свежие за сегодня) или (введите свою дату с 2012-01-01 по сегодня в таком формате (" + str(datetime.date.today()) + ")) и я выберу новую партию шуточек \nПосле чего выбери цифру от 1 до 9:")

@bot.message_handler(content_types=['text'])
def jokes(message):
    cmc = message.text
    #bot.send_message(message.chat.id, cmc[:4])
    dateToday = datetime.date.today()
    probDate = 0
    try:
        y = int(cmc[:4])
        m = int(cmc[5:7])
        d = int(cmc[8:10])
        maxDayDate = monthrange(y, m)[1]

        if 2012 <= y <= int(dateToday.year):
            probDate = 1

        if 1 <= m <= 12:
            if probDate == 1:
                probDate = 1
            else:
                probDate = 0
        else:
            probDate = 0

        if 1 <= d <= int(maxDayDate):
            if probDate == 1:
                probDate = 1
            else:
                probDate = 0
        else:
            probDate = 0
    except:
        pass


    if message.text.lower() in '123456789':
        if not list_of_jokes:
            bot.send_message(message.chat.id, "На сегодня всё. \nЕсли хотите еще =) \nможно написать (рандом - для рандомного дня) или (новые - это самые свежие за сегодня) или (введите свою дату с 2012-01-01 по сегодня в таком формате (" + str(datetime.date.today()) + ")) и я выберу новую партию шуточек \nПосле чего выбери цифру от 1 до 9:")
        else:
            #print('The list is not empty.')
            bot.send_message(message.chat.id, list_of_jokes[0])
            # random.shuffle(list_of_jokes)
            del list_of_jokes[0]
    elif message.text.lower() == 'рандом':
        startDate = datetime.date(2012, 1, 1)
        endDate = datetime.date.today()

        yearDate = ran_date(startDate.year, endDate.year)
        monthDate = ran_date(1, 12)
        dayDate = ran_date(1, monthrange(yearDate, monthDate)[1])

        monthLen = len(str(monthDate))
        if 1 == int(monthLen):
            monthDate = f"0{monthDate}"

        dayLen = len(str(dayDate))
        if 1 == int(dayLen):
            dayDate = f"0{dayDate}"

        bot.send_message(message.chat.id, f"{yearDate}-{monthDate}-{dayDate}")
        dateFull = f"{yearDate}-{monthDate}-{dayDate}"
        test(dateFull)
    elif message.text.lower() == 'новые':
        bot.send_message(message.chat.id, dateToday)
        test1()
    elif probDate == 1:
        bot.send_message(message.chat.id, message.text)
        test(message.text)
        probDate = 0
    else:
        bot.send_message(message.chat.id, "Введите любую цифру от 1 до 9 \n Или можно написать (рандом - для рандомного дня) или (новые - это самые свежие за сегодня) или (введите свою дату с 2012-01-01 по сегодня в таком формате (" + str(datetime.date.today()) + ")) и я выберу новую партию шуточек \nПосле чего выбери цифру от 1 до 9:")

bot.polling()