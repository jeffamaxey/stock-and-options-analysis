from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from flask_login import current_user
from view.general import read_field

contact_bp = Blueprint("contact", __name__)

mail = Mail()


@contact_bp.route('/contact', methods=["GET", "POST"])
def contact():
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
        mail.send(msg)

        flash("An email has been sent. Thank you for contacting us, we will respond shortly.", category="Success")
        return render_template('contact-page.html', user=current_user)

    return render_template('contact-page.html', user=current_user)
