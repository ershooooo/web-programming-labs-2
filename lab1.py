from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1',__name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
def menu():
     return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Трубицына Алиса Владимировна, Ершова Клара Александровна, лабораторная 1</title>
    </head>
    <body>
        
        <header>
            НГТУ, ФБ, Лабораторные работы, WEB-программирование, 2 часть
        </header>

        <h1>Список лабораторных</h1>
        <menu>
            <div>
                <ul>
                    <li><a href="/lab1/" target="_blank">Лабораторная работа 1</a></li>
                    <li><a href="/lab2/" target="_blank">Лабораторная работа 2</a></li>
                    <li><a href="/lab3/" target="_blank">Лабораторная работа 3</a></li>
                    <li><a href="/lab4/" target="_blank">Лабораторная работа 4</a></li>
                    <li><a href="/lab5" target="_blank">Лабораторная работа 5</a></li>
                    <li><a href="/lab6" target="_blank">Лабораторная работа 6</a></li>
                    <li><a href="/lab7/" target="_blank">Лабораторная работа 7</a></li>
                    <li><a href="/lab8/" target="_blank">Лабораторная работа 8</a></li>
                    <li><a href="/lab9/" target="_blank">Лабораторная работа 9</a></li>
                </ul>
            </div>
        </menu>

        <footer>
            &copy; Трубицына Алиса, Ершова Клара, ФБИ -12, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@lab1.route('/lab1/oak')
def oak():
     return '''
<!doctype html>
<html
    <head> 
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static' , filename='oak.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/student')
def logo():
     return '''
<!doctype html>
<html
    <head> 
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Трубицына Алиса Владимировна</h1>
        <h1>Ершова Клара Александровна</h1>
        <img src="''' + url_for('static' , filename='logo.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/python')
def python():
     return '''
<!doctype html>
<html
    <head> 
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h2>Python — это язык программирования, который широко используется в интернет-приложениях, 
        разработке программного обеспечения, науке о данных и машинном обучении (ML). 
        Разработчики используют Python, потому что он эффективен, прост в изучении и работает на разных платформах. 
        Программы на языке Python можно скачать бесплатно,
         они совместимы со всеми типами систем и повышают скорость разработки.</h2>
        <h2>Python разработан Гвидо Ван Россумом (Guido Van Rossum), программистом из Нидерландов. 
        Он начал работу над языком в 1989 году в центре Centrum Wiskunde & Informatica (CWI). 
        Изначально язык был полностью любительским проектом: Ван Россум просто хотел чем-то занять себя на рождественских каникулах. 
        Название языка было взято из телешоу BBC «Летающий цирк Монти Пайтона», 
        большим поклонником которого являлся программист. </h2>
        <img src="''' + url_for('static' , filename='python.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/zebra')
def zebra():
     return '''
<!doctype html>
<html
    <head> 
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h2>Зебра (Hippotigris) является примитивным видом лошадиного семейства. Относится к млекопитающим,
         входит в отряд непарнокопытных. Включает в себя сочетание осла и лошади</h2>

         <h2>Размер животного составляет до 2 м в длину, весит до 355 кг. Высота от 1,35 до 1,55 м. 
         Самец крупнее самки.</h2>

         <h2>Ноги короче и толще, чем у обычных скакунов с крупными, надежными копытами, голова тяжелая, крупная. 
         Сходства с ослом заключается в длинных ушах и хвосте с кисточкой на конце (50 см).</h2>

         <h2>Грива стоячая с коротким жестким волосом, расположенным от головы до хвоста. 
         Окрас контрастный — бело-черные поперечные полосы по всему телу. 
         Расцветка может немного отличаться, в зависимости от породы зебры. Шея мускулистая, крупная.</h2>

        <img src="''' + url_for('static' , filename='zebra.jpg') + '''">
    </body>
</html>
'''


@lab1.route("/lab1/")
def two():
     return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Трубицына Алиса Владимировна, Ершова Клара Александровна, лабораторная 1</title>
    </head>
    <body>
        
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h2>Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности</h2>

        <h2><a href=" http://127.0.0.1:5000/menu ">меню</a></h2>

        <h2>Реализованные роуты</h2>
        <h2><a href="/lab1/oak">/lab1/oak- дуб</a></h2>
        <h2><a href="/lab1/student">/lab1/student- студент</a></h2>
        <h2><a href="/lab1/python">/lab1/python- python</a></h2>
        <h2><a href="/lab1/zebra">/lab1/zebra- зебра</a></h2>
        <footer>
            &copy; Трубицына Алиса, Ершова Клара, ФБИ -12, 3 курс, 2023
        </footer>
    </body>
</html>
'''