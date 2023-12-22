from flask import Blueprint, render_template, request

lab9=Blueprint('lab9',__name__)

@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
    if request.method =='GET':
        return render_template('lab9/index.html')
    if request.method == 'POST':
        user_1 = request.form.get('user_1')
        gender = request.form.get('gender')
        user_2 = request.form.get('user_2')
        return render_template('lab9/postcard.html', gender=gender, user_1=user_1, user_2=user_2)

@lab9.app_errorhandler(404)
def not_found(err):
    return render_template('lab9/404.html'), 404


@lab9.app_errorhandler(500)
def server_error(err):
    return render_template('lab9/500.html'), 500

@lab9.route('/lab9/500')
def server_error():
    return render_template('lab9/500.html')





