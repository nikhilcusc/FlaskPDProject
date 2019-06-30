from flask import Flask, render_template
from forms import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/signup')
def signup():
    form = registrationForm()
    return render_template('signup.html',title='signup',form=form)

@app.route('/login')
def login():
    form = loginForm()
    return render_template('login.html',title='login',form=form)

