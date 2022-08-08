from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from wtforms.fields import EmailField
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = EmailField(
        'Email address', 
        [DataRequired(message="required"), Email(message="invalid")])
    password = PasswordField(
        'New Password', 
        [DataRequired(message="required"), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)


# @app.route("/")
# def home():
#     return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.password.data == "12345678":
            return render_template("success.html", form=login_form)
        else:
            flash('dude','error')
            return render_template("login.html", form=login_form)
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)