import smtplib
from datetime import datetime
from random import randint
import pandas


now = datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv('day32/birthday-wisher-normal-start/birthdays.csv')

birthdays_dict = {(data_row['month'], data_row['day'])
                   : data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f'day32/birthday-wisher-normal-start/letter_templates/letter_{randint(1, 3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        mail = birthday_person['email']
        connection.starttls()
        connection.login(user=mail, password='')
        msg = f'''
        Subject: HP!!!

        {contents}
        '''
        connection.sendmail(from_addr=mail, to_addrs=mail, msg=msg)
