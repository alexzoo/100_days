import smtplib
import os
import datetime as dt
import random

mail = os.getenv('GMAIL_USER')
password = os.getenv('GMAIL_PASS')
QUOTE_FILE = 'day32/quotes.txt'


def day_of_the_week(day):
    now = dt.datetime.now()
    return True if now.weekday() == day else False


def send_email(message):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(from_addr=mail, to_addrs=mail, msg=message)


def load_quotes():
    with open(file=QUOTE_FILE) as df:
        quote_list = df.readlines()
        return quote_list


random_quote = random.choice(load_quotes())

if day_of_the_week(1):
    send_email(random_quote)
