from flask import Blueprint, render_template, request, make_response
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
        error = 'Ошибка: не задана температура'
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
    error=''

    #Ошибка нулевого значения
    if weight == '':
        error = 'Не введен вес'
    else:
    #Перевод в числовой формат
        weight=int(weight)

        #Расчет скидки
        if weight > 50:
            sale = 0.9
            message = 'Применена скидка за большой объем'
        else:
            sale = 1
            message=''

        #ячмень: 12 000 руб/т;
        if corn == 'barley':
            corn = 'Ячмень'
            price = 12000 * weight * sale
        #овёс: 8 500 руб/т;
        elif corn == 'oats':
            corn = 'Овёс'
            price = 8500 * weight * sale
        #пшеница: 8 700 руб/т;
        elif corn == 'wheat':
            corn = 'Пшеница'
            price = 8700 * weight * sale
        #рожь: 14 000 руб/т.
        else:
            corn = 'Рожь'
            price = 14000 * weight * sale

        if (weight > 0) and (501 > weight):
                return render_template('4_success_corn.html',corn=corn,weight=weight,price=price,message=message)
        #Ошибки
        if weight < 0 or weight == 0:
            error = 'Неверное значение веса'
        elif weight > 500:
            error = 'Объем отсутствует в наличии'
        
    return render_template('4_corn.html',corn=corn,weight=weight,error=error)


@lab4.route('/lab4/cookies', methods=['GET','POST'])
def cookies():
    resp = make_response(render_template('cookies.html'))
    color = request.form.get('color')
    background_color = request.form.get('background-color')
    font_size = request.form.get('font-size')
    if color and background_color and font_size:
        resp.set_cookie('color',color)
        resp.set_cookie('background-color',background_color)
        resp.set_cookie('font-size',f"{font_size}px")
    return resp 