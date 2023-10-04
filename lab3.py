from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form():
    errors={}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    errorss={}
    age = request.args.get('age')
    if age == '':
        errorss['age'] = 'Заполните поле!'

    sex = request.args.get('sex')

    return render_template('form1.html', user=user, age=age, sex=sex,errors=errors,errorss=errorss)  
    

@lab3.route('/lab3/order')
def order():
    drink=request.args.get('drink')
    milk=request.args.get('milk')
    sugar=request.args.get('sugar')
    return render_template('order.html', drink=drink, milk=milk, sugar=sugar)

@lab3.route('/lab3/pay')
def pay():
    price=0
    drink=request.args.get('drink')
    #Пусть кофе стоит 120 рублей, чёрный чай — 80 рублей, зелёный — 70 рублей. 
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    #Добавка молока удорожает напиток на 30 рублей, а сахара — на 10. Тогда получим:
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    card=request.args.get('card')
    name=request.args.get('name')
    cvv=request.args.get('cvv')

    return render_template('pay.html',price=price,card=card,name=name,cvv=cvv)


@lab3.route('/lab3/succes')
def succes():
    return render_template('succes.html')