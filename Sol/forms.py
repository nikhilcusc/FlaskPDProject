#from wtforms import FlaskForm
#from flask.ext.wtf import Form
#from wtforms import *
#from wtfroms.validators import *


class registrationForm(FlaskForm):
	userName = StringField('Username',validators = [DataRequired(), Length(min=2, max=20)])
	email = StringField('Email',validators = [DataRequired(), Email()])
	passWord = StringField('Password',validators = [DataRequired()])
	confirmPassWord = StringField('Confirm Password',validators = [DataRequired(), EqualTo('passWord')])

	submit = SubmitField('Sign Up!')


class loginForm(FlaskForm):
	email = StringField('Email',validators = [DataRequired(), Email()])
	passWord = StringField('Password',validators = [DataRequired()])
	rememberMe = BooleanField('Remember Me')
	submit = SubmitField('LogIn!')
