from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, make_response, redirect, session
import psycopg2
from Db import db
from Db.models import users,articles
from flask_login import login_user, login_required, current_user

lab6 = Blueprint('lab6',__name__)

@lab6.route("/lab6/check")
def main():
    # Тоже самое, что select * from users
    my_users = users.query.all()
    print(my_users)
    return "result in console!"

@lab6.route("/lab6/check_articles")
def check_articles():
    
    my_articles = articles.query.all()
    print(my_articles)
    return "result in console!"

@lab6.route("/lab6/register",methods=["GET","POST"])
def register():
    if request.method=='GET':
        return render_template('5_register.html')

    errors = ''
    username_form=request.form.get('username')
    password_form=request.form.get('password')

    #Проверка пустых полей
    if username_form =='' or password_form == '':
        errors='Пожалуйста, заполните все поля'
        return render_template('5_register.html',errors=errors)

    '''Проверяем пользователя в БД с таким же именем
    Если такого пользователя нет, то в isUserExist вернется None 
    т.е. мы можем интерпретировать это как False'''

    '''
    select * from users
    WHERE username=username_form
    LIMIT 1 
    --где username_form - это имя, которое мы получили из форм
    '''
    #Проверка, что такой пользователь отсуствует 
    isUserExist = users.query.filter_by(username=username_form).first()
    if isUserExist is not None:
        errors='Пользователь с данным именем уже существует'
        return render_template('5_register.html',errors=errors)

    #Проверка, что пароль больше 5 символов
    if len(password_form) < 5:
        errors='Придумайте более сложный пароль'
        return render_template('5_register.html',errors=errors)
   
   #Хэшируем пароль
    hashedPswd = generate_password_hash(password_form, method='pbkdf2')
   #Создаем объект users с нужными полями 
    newUser = users(username=username_form,password=hashedPswd)

   #INSERT
    db.session.add(newUser)
   #conn.commit()
    db.session.commit()

   #Перенаправление на страницу логина
    return redirect('/lab6/login')