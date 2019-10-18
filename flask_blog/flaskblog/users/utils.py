import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_profile_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + file_ext
    picture_path = os.path.join(
        current_app.root_path, 'static/profile_pics', picture_filename)

    # resize the image for smaller
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_filename


def send_request_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='ruj@hyee.com.cn', recipients=[user.email])
    msg.body = f"""Hi,{user.username}:
    To reset your password, visit the following link,
    {url_for('users.reset_token', token=token, _external=True)}
    If you did not make this request then simply ignore this email and no changes will be made.
    """
    mail.send(msg)
