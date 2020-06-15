from flask import url_for
from flask import redirect
from flask import request
from flask import render_template
from flask import Blueprint
from flask import flash
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from AOOPMessages import db
from AOOPMessages.models import User
from werkzeug.security import check_password_hash, generate_password_hash
from AOOPMessages.forms import LoginForm , SignupForm , MessageForm
from AOOPMessages.message import message



auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    form = LoginForm(request.form)
    if current_user.is_authenticated:
        msg = message.get_messages_by_user(current_user.id)
        return render_template('profile.html',user=current_user,msg=msg)
    return render_template('login.html',form=form)


@auth.route('/login', methods=['POST'])
def login_post():

    form = LoginForm(request.form)
    messageForm = MessageForm()

    if not form.validate_on_submit():
        return render_template('login.html', form=form)

    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()

    if user is not None and check_password_hash(user.password, password):
        login_user(user)
        msg = message.get_messages_by_user(user.id)
        return render_template('profile.html', user=user,formMesaage = messageForm,msg=msg) , 200
    else:
        flash('Please check your login details and try again...')
        return redirect(url_for('auth.login'))



@auth.route('/signup', methods=["GET"])
def signup():
    form = SignupForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return render_template('signup.html',form=form)


@auth.route('/signup', methods=["POST"])
def signup_post():
    form = SignupForm(request.form)

    if not form.validate_on_submit():
        return render_template('signup.html', form=form)

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists...')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email,
                    password=generate_password_hash(password))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('main.home')) ,200


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
