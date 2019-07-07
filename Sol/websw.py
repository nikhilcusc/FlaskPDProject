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


@app.route('/chart')
def chart():
    labels = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    values = [10,9,8,7,6,4,7,8,6,4,9,2]
    return render_template('chart.html',title='chart',labels= labels, values= values)

@app.route('/charts2')
def charts2():
    labels = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    values = [10,9,8,7,6,4,7,8,6,4,9,2]
    values2 = [9,8,7,6,4,7,8,6,4,9,2,10]
    return render_template('charts3.html',title='chart',labels= labels, values= values, values2= values2)

@app.route('/linechart')
def linechart():
    labels = [1-05-12, 30-04-12,
27-04-12,26-04-12,
25-04-12, 24-04-12,
23-04-12,20-04-12,
19-04-12, 18-04-12,
17-04-12, 16-04-12,]
    values = [10,9,8,7,6,4,7,8,6,4,9,2]
    values2 = [9,8,7,6,4,7,8,6,4,9,2,10]
    return render_template('linechart.html',title='chart',labels= labels, values= values, values2= values2)

