from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
     return """
<!doctype html>
<html>
    <head>
        <title>Трубицына Алиса Владимировна, Ершова Клара Александровна, лабораторная 1</title>
    </head>
    <body>
        
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <h2>Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности</h2>

        <footer>
            &copy; Трубицына Алиса, Ершова Клара, ФБИ -12, 3 курс, 2023
        </footer>
    </body>
</html>
"""
