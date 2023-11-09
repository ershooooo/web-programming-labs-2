from flask import Blueprint, render_template, request, make_response, redirect
import psycopg2

lab5 = Blueprint('lab5',__name__)


def dbConnect():
    # Прописываем параметры подключения к БД
    conn = psycopg2.connect(
        host="127.0.0.1",
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
    visibleUser='Anon'

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
    errors=[]

    # Если это метод GET, то верни шаблон и заверши выполнение
    if request.method=='GET':
        return render_template('register.html',errors=errors)
    
    # Если мы попали сюда, значит это метод POST, так как GET мы уже обработали и сделали return.
    # После return функция немедленно завершается
    username=request.form.get('username')
    password=request.form.get('password')

    # Проверяем username и password на пустоту
    # Если любой из них пустой, то добавляем ошибку и рендерим шаблон
    if username =='' or password == '':
        errors='Пожалуйста, заполните все поля'
        return render_template('register.html',errors=errors)

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
        return render_template('register.html',errors=errors)

    # Если мы попали сюда, то значит в cur.fetchone нет ни одной строки
    # Значит пользователя с таким же логином не существует
    cur.execute(f"INSERT INTO users (username,password) VALUES ('{username}','{password}');")

    # Делаем commit - фиксируем изменения
    conn.commit()
    dbClose(cur,conn)

    return redirect('/lab5/login')
