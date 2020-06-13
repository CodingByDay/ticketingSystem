# Flask application for managing tickets
from flask import Flask, escape, request, render_template, Response

import flask

# Setting an app
app = Flask(__name__)


@app.route('/')
def hello():
    name = "ticketingSystem"
    return render_template('home.html', name=name)
    
# Definicija rute za login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return render_template('login.html')

    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User() 
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'    



        
    


    
