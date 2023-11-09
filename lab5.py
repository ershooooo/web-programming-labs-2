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


