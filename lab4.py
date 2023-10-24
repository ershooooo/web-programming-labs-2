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
    

@lab4.route('/lab4/fridge', methods=['GET','POST'])
def fridge():
    if request.method == 'GET':
        return render_template('4_fridge.html')
   
    temp = request.form.get('temp')
    error=''

    if temp == '':
        error = 'Не введен вес'
    else:
        if temp:
            temp=int(temp)
            if (temp>-13) and 0>temp:
                if (temp>-13) and (-8>temp):
                    snow = '❄️❄️❄️'
                elif (temp>-9) and (-4>temp):
                    snow = '❄️❄️'
                elif (temp>-5) and (0>temp):
                    snow = '❄️'
                return render_template('4_success_fridge.html',temp=temp,snow=snow)

            if temp <-12:
                error = 'Не удалось установить температуру: слишком низкое значение'
            if temp >-1:
                error = 'Не удалось установить температуру: слишком высокое значение'

    return render_template('4_fridge.html',temp=temp,error=error)

    


@lab4.route('/lab4/corn', methods=['GET','POST'])
def corn():
    if request.method == 'GET':
        return render_template('4_corn.html')
    
    corn=request.form.get('corn')
    weight=request.form.get('weight')
    message=''
    error=''

    #Ошибка нулевого значения
    if weight == '':
        error = 'Не введен вес'
    else:
    #Перевод в числовой формат
        weight=int(weight)

        #Ошибки
        if weight < 0 or weight == 0:
            error = 'Неверное значение веса'
        elif weight > 500:
            error = 'Объем отсутствует в наличии'
        
        #Расчет скидки
        if weight > 50:
            sale = 0.9
            message = 'Применена скидка за большой объем'
        else:
            sale = 1

        #ячмень: 12 000 руб/т;
        if corn == 'barley':
            price = 12000 * weight * sale
        #овёс: 8 500 руб/т;
        elif corn == 'oats':
            price = 8500 * weight * sale
        #пшеница: 8 700 руб/т;
        elif corn == 'wheat':
            price = 8700 * weight * sale
        #рожь: 14 000 руб/т.
        else:
            price = 14000 * weight * sale

    return render_template('4_corn.html',corn=corn,weight=weight,price=price,message=message,error=error)