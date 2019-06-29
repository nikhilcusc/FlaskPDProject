from flask import Flask
app = Flask(__name__)

@app.route('/')

#def hello_world():
#    return 'Hello, World!2'
def hello():
    return 'Sol/Hello World1 w!'

