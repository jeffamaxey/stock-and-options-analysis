from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for,
from flask.ext.mail import Message, Mail

mail = Mail()

app = Flask(__name__)
app.secret_key = 'dev key 123'

# Use Message and Mail with Flask-Mail imports to config SMTP settings
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = Truecoj
app.config["MAIL_USERNAME"] = 'temp_email@gmail.com'
app.config["MAIL_PASSWORD"] = 'put_password_here'

mail.init_app(app)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    # Reads the input data when the user presses the submit button
    if request.method == 'POST':
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        if len(email) == 0:
            flash("Please enter your email address.", category="Error")
        elif len(subject) == 0:
            flash("Please enter a subject.", category="Error")
        elif len(message) == 0:
            flash("Please enter a message.", category="Error")

        else:

            msg = Message(subject.data, sender='temp_email@gmail.com', recipients=['official_company_email@gmail.com'])
        msg.body = """
        <%s>
      %s
      """ % (email.data, message.data)
        mail.send(msg)

        flash("An email been sent from " + str(email) + ".", category="Success")
        return render_template('contact-page.html', form=form)

# Go to contact page
elif request.method == 'GET':
return render_template('contact-page.html', form=form)
