from flask import Flask, render_template, Markup
import pandas as pd



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
@app.route('/chartjs')
def chartjs():
    dataxls = pd.read_excel (r'/home/fortknox/Documents/PD/PD_challenge/PD_challange_dataset.xlsx')
    df = pd.DataFrame(dataxls)
    df.fillna(0)
    temperature = []
    consumption = []
    time = []
    for iter1, iter2 in df.iterrows():
        temperature.append(iter2.out_door_temp)
        consumption.append(iter2.electricity_usage)
        temptime = iter2.time 
        temptime = temptime.ctime()
        time.append(temptime)
    labels = [01-05-12, 30-04-12,
27-04-12,26-04-12,
25-04-12, 24-04-12,
23-04-12,20-04-12,
19-04-12, 18-04-12,
17-04-12, 16-04-12]
    values = [1,10,9,8,2,6,4,7,8,6,4,9]
    values2 = [0,9,8,2,6,4,7,8,6,4]
    return render_template('chartjs1.html',title='chartjs',time= time[:1000], consumption= consumption[:1000], temperature= temperature[:1000])

@app.route('/linechart')
def linechart():
    dataxls = pd.read_excel (r'/home/fortknox/Documents/PD/PD_challenge/PD_challange_dataset.xlsx') 
    df = pd.DataFrame(dataxls)
    #df.fillna(0)
    temperature = []
    consumption = []
    time = []
    for iter1, iter2 in df.iterrows():
        temperature.append(iter2.out_door_temp)
        consumption.append(iter2.electricity_usage)
        temptime = iter2.time 
        temptime = temptime.ctime()
        time.append(temptime) 
    labels = [1-05-12, 30-04-12,
27-04-12,26-04-12,
25-04-12, 24-04-12,
23-04-12,20-04-12,
19-04-12, 18-04-12,
17-04-12, 16-04-12]
    values = [0,10,9,8,2,6,4,7,8,6,4,9]
    values2 = [0,9,8,2,6,4,7,8,6,4,9,2]
    return render_template('linechart.html',temperature= temperature[10000:],consumption= consumption, time= time, title='chart',labels= labels, values= values, values2= values2)


@app.route('/zoomablelinechart')
def zoomablelinechart():
    dataxls = pd.read_excel (r'/home/fortknox/Documents/PD/PD_challenge/PD_challange_dataset.xlsx') 
    df = pd.DataFrame(dataxls)
    df.fillna(0)
    temperature = []
    consumption = []
    time = []
    for iter1, iter2 in df.iterrows():
        temperature.append(iter2.out_door_temp)
        consumption.append(iter2.electricity_usage)
        temptime = iter2.time 
        temptime = temptime.ctime()
        time.append(temptime) 
    labels = [1-05-12, 30-04-12,
27-04-12,26-04-12,
25-04-12, 24-04-12,
23-04-12,20-04-12,
19-04-12, 18-04-12,
17-04-12, 16-04-12]
    values = [0,10,9,8,2,6,4,7,8,6,4,9]
    values2 = [0,9,8,2,6,4,7,8,6,4,9,2]
    return render_template('zoomablelinechart.html',temperature= temperature,consumption= consumption, time= time, title='chart',labels= labels, values= values, values2= values2)

