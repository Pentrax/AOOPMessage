from flask import url_for
from flask import redirect
from flask import request
from flask import render_template
from flask import Blueprint
from flask import flash
from flask_login import current_user
from AOOPMessages import db
from AOOPMessages.models import User , Message
from werkzeug.security import check_password_hash, generate_password_hash
from AOOPMessages.forms import SignupForm , MessageForm


message = Blueprint('message', __name__)

@message.route('/send', methods=['POST'])
def send_message():

    messageForm = MessageForm(request.form)

    to = request.form['to']


    user_to =User.query.filter_by(email=to).first()

    author_id = request.form['author_id']
    user = User.query.filter_by(id=author_id).first()

    if not user_to:
        flash('The user who is trying to send the message does not exist')
        return render_template('message.html', formMesaage=messageForm, user=user)

    if  messageForm.validate_on_submit():
        user_to_id = User.query.filter_by(email=request.form["to"]).first()
        new_message = Message(
                            title = request.form["title"],
                            body  = request.form["body"],
                            author_id = request.form["author_id"] ,
                            to_id   =   user_to_id.id,
                            author_name = user.email
                            )

        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('auth.login')),200


@message.route("/message",methods=['GET'])
def message_form():

    messageForm = MessageForm(request.form)
    user_response = request.args.get('current_response')
    email = False

    if user_response:
        user_response= User.query.filter_by(id=user_response).first()
        email = user_response.email

    if current_user.is_authenticated:
        user = current_user
        return render_template('message.html', formMesaage=messageForm,user=user,email = email)




def get_messages_by_user(user_id):
    messages = Message.query.filter_by(to_id=user_id).order_by(Message.timestamp.desc()).all()

    return messages