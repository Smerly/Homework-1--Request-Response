from flask import Flask
from random import randint
app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f"Wow, {users_animal} is my favorite animal too!"


@app.route('/dessert/<donuts>')
def favorite_dessert(donuts):
    return f'How did you know I liked {donuts}?'


@app.route('/madlibs/<adjective>/<noun>')
def mad_lib(adjective, noun):
    return f'Wait, whats a madlib? Oh! I know! It\'s a {adjective} {noun}'


@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    number1 = str(number1)
    number2 = str(number2)
    if number1.isdigit() and number2.isdigit():
        numbernum1 = int(number1)
        numbernum2 = int(number2)
        product = numbernum1 * numbernum2
        numberstr1 = str(number1)
        numberstr2 = str(number2)
        productstr = str(product)
        return f'{numberstr1} x {numberstr2} = {productstr}'
    else:
        return f'Looks like one of the inputted numbers is not a number! Try again with a number'


@app.route('/sayntimes/<word>/<n>')
def say_n(word, n):
    if n.isdigit():
        speak = (str(word) + ' ') * int(n)
        return f'{speak}'
    else:
        return f'Try to put in a word and a number!'


@app.route('/dicegame')
def roll():
    single = randint(1, 6)
    if single == 6:
        return f'You rolled {single}! You win!'
    else:
        return f'You rolled {single}. You lost :('


if __name__ == '__main__':
    app.run(debug=True)
