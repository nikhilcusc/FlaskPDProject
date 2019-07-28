from flask import Flask, render_template, Markup
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


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
    
    return render_template('chartjs1.html',title='chartjs',time= time, consumption= consumption, temperature= temperature)
