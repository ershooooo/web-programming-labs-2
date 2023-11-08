from flask import Blueprint, render_template, request, make_response, redirect
import psycopg2

lab5 = Blueprint('lab5',__name__)


@lab5.route('/lab5')
def main():
#Прописываем параметры подключения к БД
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_ersh_trub",
        user="ersh_trub_knowledge_base",
        password="ershtrub123")

#Получаем курсор. С помощью него мы можем выполнять sql-запросы
    cur=conn.cursor()

#Пишем запрос, который psycopg2 должен выполнить
    cur.execute("SELECT * FROM users;")
# fetchall - получить все строки, которые получились в результате выполнения sql -запроса в execute
# Сохраняем эти строки в перемннную RESULT
    result=cur.fetchall()

#Закрываем соеденения с БД
    cur.close()
    conn.close()

    print(result)
    return "go to console"

@lab5.route('/lab5/users')
def get_users():

    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_ersh_trub",
        user="ersh_trub_knowledge_base",
        password="ershtrub123")
    cur = conn.cursor()
    
    cur.execute("SELECT username FROM users;")
    result = cur.fetchall()

    cur.close()
    conn.close()

    username = ""
    for row in result:
        username += f"{row[0]}\n"
    return username