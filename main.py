from unicodedata import name
from flask import Flask, render_template, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, Field
from wtforms_alchemy import PhoneNumberField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from wtforms.fields import EmailField
from flask_bootstrap import Bootstrap
import phonenumbers
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

#LOGIN MANAGEMENT
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

#INSTANCES
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


class LoginForm(FlaskForm):
    email = EmailField(
        'Email', 
        [DataRequired(message="Please insert a valid email address"), Email(message="Invalid email address")],
        id='email',)
    password = PasswordField(
        'Password', 
        [DataRequired(message="Please insert a valid password"), Length(min=8, message="Length too short, minimum 8 characters!")])
    submit = SubmitField(label="Log In")

class MainForm(FlaskForm):
    firstName = StringField(
        'First Name',
        [DataRequired(message="Please insert a name")])
    lastName = StringField(
        'Last Name',
        [DataRequired(message="Please insert a name")])
    dateOfBirth = DateField(
        "Date of Birth",
        [DataRequired(message="Please insert your birthday")])
    phone = PhoneNumberField(
        'Phone Number 📞',
        [DataRequired(message="Please insert a phone number")],
        region= 'US',
        display_format='national')
    submit_2 = SubmitField('Submit')
    country = StringField(
        'Country',
        [DataRequired(message="Please insert your country")])
    city = StringField(
        'City',
        [DataRequired(message="Please insert your city")])
    zip = StringField(
        'ZIP',
        [DataRequired(message="Please insert a valid ZIP code")])

app = Flask(__name__)
app.secret_key = "thisisasecretkey"
Bootstrap(app)

@app.route("/", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    main_form = MainForm()
    if login_form.validate_on_submit():
        email_input = login_form.email.data
        pass_input = login_form.password.data
        print(email_input)
        print(pass_input)
        if login_form.password.data == "12345678":
            return render_template("index.html", form=main_form)
        else:
            flash('Wrong password, please try again','error')
            return render_template("login.html", form=login_form)
    return render_template("login.html", form=login_form)



if __name__ == '__main__':
    app.run(debug=True)