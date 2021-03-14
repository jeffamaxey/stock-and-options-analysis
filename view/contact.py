from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from flask_login import current_user

contact_bp = Blueprint("contact", __name__)

mail = Mail()

"""
This function checks all input fields on contact-page.html and if they are correctly filled in, will send a message to a company email.
"""
@contact_bp.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':

        # Checking email input field is filled for all page format types
        email = request.form.get("email11")
        if email is None:
            email = request.form.get("email18")
        if email is None:
            email = request.form.get("email113")
        if email is None:
            email = request.form.get("email118")

        # Checking subject input field is filled for all page format types
        subject = request.form.get("subject1")
        if subject is None:
            subject = request.form.get("subject11")
        if subject is None:
            subject = request.form.get("subject12")
        if subject is None:
            subject = request.form.get("subject13")

        # Checking message input field is filled for all page format types
        message = request.form.get("write-your-message-here1")
        if message is None:
            message = request.form.get("write-your-message-here11")
        if message is None:
            message = request.form.get("write-your-message-here12")
        if message is None:
            message = request.form.get("write-your-message-here13")

        # If past all prior if-statements, prepare to send message
        msg = Message(subject, recipients=['thefintechorgtest@gmail.com'])

        # for message format
        msg.body = """ From: <%s> 
            %s """ % (email, message)
        mail.send(msg)

        flash("An email has been sent. Thank you for contacting us, we will respond shortly.", category="Success")
        return render_template('contact-page.html', user=current_user)

    # load up contact page
    return render_template('contact-page.html', user=current_user)
