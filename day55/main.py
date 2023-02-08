from random import randint
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''
     <h1>Guess a number between 0 and 9</h1>
     <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">
     '''


rand_num = randint(0, 9)


@app.route('/<int:number>')
def show_number(number):

    if number < rand_num:
        return f'''
        <font color='red'>
        <h1>Too Low, try again!</h1>
        <h1>Guessed num: {rand_num}</h1>
        </font>
        <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>
        '''
    elif number > rand_num:
        return f'''
        <font color='blue'>
        <h1>Too high, try again!</h1>
        <h1>Guessed num: {rand_num}</h1>
        </font>
        <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>
        '''
    else:
        return f'''
        <font color='green'>
        <h1>Got it, correct!</h1>
        <h1>Guessed num: {rand_num}</h1>
        </font>
        <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>
        '''


def make_bold(func):
    def wrapper():
        return f'<b>{func()}</b>'
    return wrapper


def make_emphasis(func):
    def wrapper():
        return f'<em>{func()}</em>'
    return wrapper


def make_underline(func):
    def wrapper():
        return f'<u>{func()}</u>'
    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return 'Bye!'


if __name__ == '__main__':
    app.run(debug=True)
