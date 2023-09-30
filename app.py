from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

@app.route('/lab2/example')
def example():
    name, number, group, cours = 'Трубицына Алиса, Ершова Клара','Лабораторная работа 2', 'ФБИ-12', '3 курс'
    fruits =[
         {'name':'яблоки','price':100},
         {'name':'груши','price':120},
         {'name':'апельсины','price':80},
         {'name':'мандарины','price':95},
         {'name':'манго','price':350}
         ]
    books =[
         {'name': 'Бесы','author': 'Федор Достоевский','style': 'роман','page':704},
         {'name': 'Мартин Иден','author': 'Джек Лондон ','style': 'роман','page':416},
         {'name': 'Братья Карамазовы','author': 'Федор Достоевский','style': 'роман','page':832},
         {'name': 'Тридцатилетняя женщина','author': 'Оноре де Бальзак','style': 'роман','page':384},
         {'name': 'Палата №6','author': 'Антон Чехов','style': 'повесть','page':416},
         {'name': 'Голем','author': 'Густав Майринк','style': 'роман','page':320},
         {'name': 'Гроза','author': 'Александр Островский','style': 'трагедия','page':416},
         {'name': 'Черный обелиск','author': 'Эрих Мария Ремарк','style': 'роман','page':416},
         {'name': 'Фауст','author': 'Иоганн Вольфганг Гете','style': 'трагедия','page':544},
         {'name': 'Процесс','author': 'Франц Кафка','style': 'роман','page':320}
    ]   
    return render_template('example.html', number=number,name=name,group=group,cours=cours, fruits=fruits,books=books)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/pictures')
def pictures():
    return render_template('pictures.html')
   
@app.route('/lab2/zach_2')
def zach_2():
    A,B,C,N,K,G,H,summa=2,4,6,4,6,2,5,0
    if A<B<C:
        A=A*2
        B=B*2
        C=C*2

    result=str(N)*K

    for i in range(1, H+1):
        summa += i**G

    slovar=[{'A':A,'B':B,'C':C,'summa':summa,'result':result}]
    return render_template('zach_2.html',slovar=slovar)
