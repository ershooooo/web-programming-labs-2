from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4',__name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('4_login.html')

    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'ershtrub' and password == '555':
        return render_template('4_success.html',username=username)
    
    error = ''
    if username != 'ershtrub' or password != '555':
        error = 'Неверный логин и/или пароль'
    if username == '':
        error = 'Не введен логин!'
    if password == '':
        error = 'Не введен пароль!'
    
    return render_template('4_login.html', error=error,username=username,password=password)
    

    
