from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from wtforms.fields import EmailField
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = EmailField(
        'Email', 
        [DataRequired(message="Please insert a valid email address"), Email(message="Invalid email address")],
        id='email',)
    password = PasswordField(
        'Password', 
        [DataRequired(message="This field is empty"), Length(min=8, message="Length too short, minimum 8 characters!")])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)



@app.route("/", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.password.data == "12345678":
            return render_template("success.html", form=login_form)
        else:
            flash('Wrong password, please try again','error')
            return render_template("login.html", form=login_form)
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)