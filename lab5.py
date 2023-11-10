from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, make_response, redirect, session
import psycopg2

lab5 = Blueprint('lab5',__name__)


def dbConnect():
    # Прописываем параметры подключения к БД
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5433",
        database="knowledge_base_for_ersh_trub",
        user="ersh_trub_knowledge_base",
        password="ershtrub123")
    return conn


def dbClose(cursor,connection):
    # Закрываем курсор и соединение 
    cursor.close()
    connection.close()


@lab5.route('/lab5')
def main():
    username=session.get("username")
    if username =='':
        visibleUser='Anon'
    else:
        visibleUser=username
    return render_template('5_main.html',username=visibleUser)

@lab5.route('/lab5/users')
def get_users():

    conn = dbConnect()
    cur = conn.cursor()
    
    cur.execute("SELECT username FROM users;")
    result = cur.fetchall()

    dbClose(cur,conn)

    username = ""
    for row in result:
        username += f"{row[0]}\n"
    return username


@lab5.route('/lab5/register', methods=['GET','POST'])
def registerPage():
    errors=''

    # Если это метод GET, то верни шаблон и заверши выполнение
    if request.method=='GET':
        return render_template('5_register.html',errors=errors)
    
    # Если мы попали сюда, значит это метод POST, так как GET мы уже обработали и сделали return.
    # После return функция немедленно завершается
    username=request.form.get('username')
    password=request.form.get('password')

    # Проверяем username и password на пустоту
    # Если любой из них пустой, то добавляем ошибку и рендерим шаблон
    if username =='' or password == '':
        errors='Пожалуйста, заполните все поля'
        return render_template('5_register.html',errors=errors)

    # Получаем пароль от пользователя, хэруем его
    hashPassword = generate_password_hash(password)

    # Если мы попали сюда, значит username и password заполнены
    # Подключаемся к БД
    conn = dbConnect()
    cur = conn.cursor()

    # Проверяем наличие клиента в базе. У нас не может быть два пользователя с одинаковыми логинами
    # WARNING: мы используем f-строки, что не рекомендуется делать 
    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    # fetchone, в отличие от fetchall, получает только одну строку
    # мы задали свойство UNIQUE для пользователя, значитбольше одной строки мы не можем получить 
    # Только один пользователь с таким именем может быть в БД
    if cur.fetchone() is not None:
        errors='Пользователь с данным именем уже существует'
        
        dbClose(cur,conn)
        return render_template('5_register.html',errors=errors)

    # Если мы попали сюда, то значит в cur.fetchone нет ни одной строки
    # Значит пользователя с таким же логином не существует
    cur.execute(f"INSERT INTO users (username,password) VALUES ('{username}','{hashPassword}');")

    # Делаем commit - фиксируем изменения
    conn.commit()
    dbClose(cur,conn)

    return redirect('/lab5/login')



@lab5.route('/lab5/login', methods=['GET','POST'])
def loginPage():
    errors=''

    if request.method=='GET':
        return render_template('5_login.html',errors=errors)
    
    username=request.form.get('username')
    password=request.form.get('password')

    if username =='' or password == '':
        errors='Пожалуйста, заполните все поля'
        return render_template('5_login.html',errors=errors)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}'")

    result = cur.fetchall()

    if not result:
        errors='Неправильный логин или пароль'
        dbClose(cur,conn)
        return render_template('5_login.html',errors=errors)

    userID = result[0][0]
    hashPassword = result[0][1]

    # Сравниваем хэш и пароль
    if check_password_hash(hashPassword,password):
        # Сохраняем id и username в сессию 
        session['id']=userID
        session['username']=username
        dbClose(cur,conn)
        return redirect('/lab5')

    else:
        errors='Неправильный логин или пароль'
        return render_template('5_login.html',errors=errors)


#Создание роута для добавления статей
@lab5.route("/lab5/new_article", methods=['GET','POST'])
def createArticle():
    errors = ''
#Проверяем авторизирован ли пользователь
#Мы читаем из JWT токена(session.get) ID пользователя
    userID = session.get("id")
    if userID is not None:
#Пользователь авторизирован, мы прочитали jwt-токен
#Проверили его валидность. Получили его id.
        if request.method == "GET":
            return render_template("new_article.html")
        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")
            if len(text_article) == 0:
                errors = 'Заполните текст'
                return render_template("new_article.html", errors=errors)
            conn = dbConnect()
            cur = conn.cursor()

            cur.execute(f"INSERT INTO articles(user_id, title, article_text) VALUES ({userID}, '{title}','{text_article}') RETURNING id")
#Получаем id от вновь созданной записи
#В нашем случае мы будем получать статьи следующим образом
#/lab5/articles/id_articles
            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur,conn)
#Делаем редирект на новую статью
#Пока этот роут не сделан, будет ошибка
#Чтобы получить статью под номером 5, необходимо ввести в роут /lab5/articles/5
            return redirect(f"/lab5/articles/{new_article_id}")
#Пользователь не авторизирован, отправить на страницу логина
    return redirect("/lab5/login")

@lab5.route("/lab5/articles/<string:article_id>")
def getArticle(article_id):
    userID = session.get("id")
    if userID is not None:
        conn = dbConnect()
        cur =conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s",(article_id, userID))
        articleBody = cur.fetchone()
        dbClose(cur,conn)

        if articleBody is None:
            return "Not found!"
#Разбиваем строку на массив по "Enter", чтобы с помощью цикла for в jinja разбить статью на параграфы
        text = articleBody[1].splitlines()

        return render_template("articleN.html", article_text=text,article_title=articleBody[0], username=session.get("username"))

@lab5.route("/lab5/spisok_article") 
def seeArticle(): 
    userID = session.get("id") 
 
    if userID is not None: 
        conn = dbConnect() 
        cur = conn.cursor() 
        cur.execute(f"SELECT title FROM articles WHERE user_id = '{userID}'") 
 
        articleBody = cur.fetchall() 
 
        dbClose(cur,conn) 
 
        if articleBody is None: 
            return "Not found!" 
        return render_template("spisok_article.html", article_title=articleBody,article_id = id, username=session.get("username"))

@lab5.route("/lab5/logout")
def logOut():

    session.clear()
    return render_template('5_login.html')
    