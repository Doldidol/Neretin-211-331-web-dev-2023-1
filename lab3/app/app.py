
from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Для доступа к этой странице нужно авторизироваться.'
login_manager.login_message_category = 'warning'

# Глобальный объект session - это словарь, который позволяет 
# сохранять данные между запросами. Flask сохраняет данные 
# сессии в cookie-файле на стороне клиента и передает его 
# обратно на сервер при следующем запросе.



# `UserMixin` - класс-помощник из пакета Flask-Login, который 
# добавляет к классу `User` необходимые методы и свойства для 
# работы с пользователем в системе аутентификации Flask.
# Класс `User` может содержать различные поля, такие как имя 
# пользователя, пароль и т.д. 
class User(UserMixin):
    def __init__(self, user_id, user_login):
        self.id = user_id
        self.login = user_login

# is_authenticated 
# Это свойство должно возвращать значение True, 
# если пользователь прошел проверку подлинности, 
# т.е. предоставил действительные учетные данные. 
# (Только прошедшие проверку подлинности пользователи 
# будут соответствовать критериям login_required.)

# is_active
# Это свойство должно возвращать значение True, если 
# это активный пользователь - в дополнение к аутентификации, 
# он также активировал свою учетную запись, не был приостановлен 
# или при каких-либо других условиях, установленных вашим 
# приложением для отклонения учетной записи. Неактивные учетные 
# записи могут не входить в систему (конечно, без принуждения).

# is_anonymous - 
# Это свойство должно возвращать значение True, если это 
# анонимный пользователь. (Вместо этого фактические 
# пользователи должны возвращать значение False.)

# get_id()
# Этот метод должен возвращать str, который однозначно 
# идентифицирует этого пользователя и может быть использован 
# для загрузки пользователя из обратного вызова user_loader. 
# Обратите внимание, что это должен быть str - если идентификатор 
# изначально является int или каким-либо другим типом, вам нужно будет 
# преобразовать его в str.       

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visits')
def visits():
    if 'visits_count' in session:
        session['visits_count'] += 1
    else:
        session['visits_count'] = 1
    return render_template('visits.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        remember = request.form.get('remember_me') == 'on'
        for user in get_users():
            if user['login'] == login and user['password'] == password:
                login_user(User(user['id'], user['login']), remember = remember)
                flash('Вы успешно прошли аутентификацию!', 'success')
                param_url = request.args.get('next')
                return redirect(param_url or url_for('index'))
        flash('Введён неправильный логин или пароль.', 'danger')
    return render_template('login.html')
# flash() - функция Flask, которая используется для 
# вывода сообщений пользователю. Она сохраняет сообщение 
# в сессии и может быть использована для сообщения о 
# успешной операции, ошибке или другой информации.


# logout_user - функция, также из библиотеки Flask-Login, 
# которая разлогинивает текущего пользователя и удаляет 
# его сессионную переменную.
@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/secret_page')
@login_required
def secret_page():
    return render_template('secret_page.html')

# Для каждого пользователя в списке проверяется, 
# совпадает ли его идентификатор (user['id']) с 
# переданной user_id. Если совпадение найдено, 
# создается и возвращается объект пользователя User с использованием 
# данных из словаря пользователя (например, идентификатор и логин).
@login_manager.user_loader
def load_user(user_id):
    for user in get_users():
        if user['id'] == int(user_id):
            return User(user['id'], user['login'])
    return None

def get_users():
    users = [{
        "id": 1,
        "login": "user",
        "password": "qwerty",
    }]
    return users