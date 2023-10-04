from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form():
    user = request.args.get('user')
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex)  
    