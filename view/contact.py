from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Message, Mail
from flask_login import current_user

contact_bp = Blueprint("contact", __name__)

mail = Mail(contact_bp)

@contact_bp.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':

        email = request.form.get("email11")
        if email is None:
            email = request.form.get("email18")
        if email is None:
            email = request.form.get("email113")
        if email is None:
            email = request.form.get("email118")

        subject = request.form.get("subject1")
        if subject is None:
            subject = request.form.get("subject11")
        if subject is None:
            subject = request.form.get("subject12")
        if subject is None:
            subject = request.form.get("subject13")

        message = request.form.get("write-your-message-here1")
        if message is None:
            message = request.form.get("write-your-message-here11")
        if message is None:
            message = request.form.get("write-your-message-here12")
        if message is None:
            message = request.form.get("write-your-message-here13")

        if len(email) == 0:
            flash("Please enter your email address.", category="Error")
        elif len(subject) == 0:
            flash("Please enter a subject.", category="Error")
        elif len(message) == 0:
            flash("Please enter a message.", category="Error")

        else:
            msg = Message(sender='TheFinTechOrgTest@gmail.com', recipients=['TheFinTechOrgTest@gmail.com'])
        msg.body = """ From: %s 
        %s """ % (email.data, message.data)
        mail.send(msg)

        flash("An email has been sent. Thank you for contacting us, we will respond shortly.", category="Success")
        return render_template('contact-page.html', user=current_user)

    return render_template('contact-page.html', user=current_user)
