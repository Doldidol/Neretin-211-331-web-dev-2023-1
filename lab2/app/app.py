from flask import Flask, render_template, request
from flask import make_response

app = Flask(__name__)
application = app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/headers')
def headers():
    return render_template('headers.html')

@app.route('/args')
def args():
    return render_template('args.html')

@app.route('/cookies')
def cookies():
    resp = make_response(render_template('cookies.html'))
    if "name" in request.cookies:
        resp.delete_cookie("name")
    else:
        resp.set_cookie("name", "value")
    return resp

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    answer=''
    error_text=''
    if request.method=='POST':
        try:
            first_num = int(request.form['firstnumber'])
            second_num = int(request.form['secondnumber'])
        except ValueError:
            error_text='Был передан текст. Введите, пожалуйста, число.'
            return render_template('calc.html', answer=answer, error_text=error_text)
        operation = request.form['operation']
        if operation == '+':
            answer = first_num + second_num
        elif operation == '-':
            answer = first_num - second_num
        elif operation == '*':
            answer = first_num * second_num
        elif operation == '/':
            try:
                answer = first_num / second_num
            except ZeroDivisionError:
                error_text = 'На ноль делить нельзя'
    return render_template('calc.html', answer=answer, error_text=error_text)

@app.route('/phone', methods=['GET', 'POST'])
def phone():
    if request.method == 'POST':
        phone_number = request.form['phone']
        formatted_number, error_message = format_validate(phone_number)
        if error_message:
            return render_template('phone.html', error=error_message, phone=phone_number)
        else:
            return render_template('phone.html', number=formatted_number)
    else:
        return render_template('phone.html')


def format_validate(number):
    allowed_chars = ' ()-.+0123456789'

    for i in number:
        if i not in allowed_chars:
            return None, 'Недопустимый ввод. В номере телефона встречаются недопустимые символы.'

    sim = ''
    for i in number:
        if i.isdigit():
            sim += i

    if len(sim) not in (10, 11):
        return None, 'Недопустимый ввод. Неверное количество цифр.'

    if len(sim) == 11 and sim.startswith('7'):
        sim = '8' + sim[1:]

    if len(sim) == 10:
        sim = '8' + sim

    formatted_number = ''

    if sim.startswith('+7'):
        formatted_number = '8-{}-{}-{}-{}'.format(sim[2:5], sim[5:8], sim[8:10], sim[10:])

    elif sim.startswith('8'):
        formatted_number = '8-{}-{}-{}-{}'.format(sim[1:4], sim[4:7], sim[7:9], sim[9:])
    else:
        return None, 'Недопустимый ввод. Неверный код страны или номера.'

    return formatted_number, None


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
