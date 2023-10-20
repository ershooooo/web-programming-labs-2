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

    return render_template('3_form1.html', user=user, age=age, sex=sex,errors=errors,errorss=errorss)  
    

@lab3.route('/lab3/order')
def order():
    drink=request.args.get('drink')
    milk=request.args.get('milk')
    sugar=request.args.get('sugar')
    return render_template('3_order.html', drink=drink, milk=milk, sugar=sugar)

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

    return render_template('3_pay.html',price=price,card=card,name=name,cvv=cvv)


@lab3.route('/lab3/succes')
def succes():
    return render_template('3_succes.html')

@lab3.route('/lab3/bilet')
def bilet():
    errors={}
    FIO=request.args.get('FIO')
    if FIO == '':
        errors['FIO'] = 'Заполните поле!'

    age=request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    
    wherefrom=request.args.get('wherefrom')
    if wherefrom == '':
        errors['wherefrom'] = 'Заполните поле!'
    
    whereto=request.args.get('whereto')
    if whereto == '':
        errors['whereto'] = 'Заполните поле!'
    
    date=request.args.get('date')
    if date == '':
        errors['date'] = 'Заполните поле!'
    
    type=request.args.get('type')
    place=request.args.get('place')
    things=request.args.get('things')
    return render_template('3_bilet.html',FIO=FIO,age=age,wherefrom=wherefrom,whereto=whereto,date=date,type=type,place=place,things=things,errors=errors)


@lab3.route('/lab3/zach_3')
def zach_3():
    n1=request.args.get('n1')
    n2=request.args.get('n2')
    n3=request.args.get('n3')
    n4=request.args.get('n4')

    if n1 and n2 and n3 and n4: 
        n1=float(n1)
        n2=float(n2)
        n3=float(n3)
        n4=float(n4)

    numb=[n1,n2,n3,n4]
    reslt=[]
    for i in range (len(numb)):
        if numb.count(numb[i])==1:
            reslt=i+1
    return render_template('zach_3.html',reslt=reslt,numb=numb,n1=n1,n2=n2,n3=n3,n4=n4)


@lab3.route('/lab3/zach_3_1')
def zach_3_1():
    n=request.args.get('n')
    x=request.args.get('x')
    factorial = 1

    if x is not None and n is not None:
        n=int(n)
        x=float(x)
        res=x

        for i in range (n):
            factorial*=2*n+1
            res+=((-1**i)*(x**(2*i+1)))/factorial

    print(res)
    return render_template('zach_3_1.html',res=res,n=n,x=x)

    