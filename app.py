# Flask application for managing tickets
from flask import Flask, escape, request, render_template

app = Flask(__name__)
#
@app.route('/')
def hello():
    name = "ticketingSystem"
    return render_template('home.html', name=name)
    
# Definicija rute za login
@app.route('/login')
def login():
    return render_template('login.html')


    
