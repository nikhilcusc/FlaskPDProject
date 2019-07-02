from flask import Flask, render_template, Markup
#from forms import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html',title='About')
@app.route('/signup')
def signup():
    #form = registrationForm()
    return render_template('signup.html',title='signup')

@app.route('/login')
def login():
    #form = loginForm()
    return render_template('login.html',title='login')


@app.route('/charts')
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html',title='chart')


