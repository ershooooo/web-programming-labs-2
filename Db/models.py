#Импортируем переменную db из файла __init.py__
from . import db
from flask_login import UserMixin

#Описываем схему нашей БД в виде оюъектов таким образом, создание таблиц (схемы БД)
#Возьмет на себя SQLAlchemy - система ORM.abs

class users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(102), nullable=False)

    def __repr__(self):
        return f'id:{self.id}, username:{self.username}'
        

class articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(50), nullable=False)
    article_text = db.Column(db.Text, nullable=False)
    is_favorite = db.Column(db.Boolean, default=False)
    is_public = db.Column(db.Boolean, default=False)
    likes = db.Column(db.Integer)

    def __repr__(self):
        return f'id:{self.id},title:{self.title}, article_text:{self.article_text}'