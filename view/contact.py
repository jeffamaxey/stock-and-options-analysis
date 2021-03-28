"""
Author: Adam Bouthillette
"""
from flask import Blueprint, render_template, request, flash
from flask_mail import Mail, Message
from flask_login import current_user
from view.general import read_field

contact_bp = Blueprint("contact", __name__)

__mail = Mail()


def init(app):
    """
    Initializes the flask mail package
    :param app: flask app
    """
    # Use Message and Mail with Flask-Mail imports to config SMTP settings
    app.config["MAIL_SERVER"] = 'smtp.gmail.com'
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config['MAIL_USE_TLS'] = False
    app.config["MAIL_USERNAME"] = 'thefintechorgtest@gmail.com'
    app.config["MAIL_PASSWORD"] = 'FTO12345'
    app.config['MAIL_DEFAULT_SENDER'] = 'thefintechorgtest@gmail.com'
    __mail.init_app(app)


@contact_bp.route('/contact', methods=["GET", "POST"])
def contact():
    """
    Takes data from contact-page.html input fields and formats for email sending.
    """
    if request.method == 'POST':
        email = read_field(("email11", "email18", "email113", "email118"))
        subject = read_field(("subject1", "subject11", "subject12", "subject13"))
        message = read_field(("write-your-message-here1", "write-your-message-here11",
                              "write-your-message-here12", "write-your-message-here13"))

        # Send message from contact page with specified recipient
        msg = Message(subject, recipients=['thefintechorgtest@gmail.com'])

        # for message format
        msg.body = """ From: %s 
        %s """ % (email, message)
        __mail.send(msg)

        flash("An email has been sent. Thank you for contacting us, we will respond shortly.", category="Success")
        return render_template('contact-page.html', user=current_user)

    return render_template('contact-page.html', user=current_user)
