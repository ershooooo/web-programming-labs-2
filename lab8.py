from flask import Blueprint, render_template, request, abort

lab8=Blueprint('lab8',__name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')

courses = [
    {"name": "c++", "videos": 3,"price": 3000},
    {"name": "basic", "videos": 30,"price": 0},
    {"name": "c#", "videos": 8} #если цена не указана, то курс бесплатный
]

#Весь список курсов
@lab8.route('/lab8/api/courses/', methods=['GET'])
def  get_courses():
    return courses

#Конкретный курс по номеру
@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    if course_num < 0 or course_num > len(courses)-1:
        abort(404, "Course not found")
    return courses[course_num]

#Удаление курса
@lab8.route('/lab8/api/courses/<int:course_num>',methods=['DELETE'])
def del_course(course_num):
    del courses[course_num]
    return '', 204