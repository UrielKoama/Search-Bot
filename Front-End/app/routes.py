from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/sports')
def sports():
    return render_template('searchpage.html', title='Sports')

@app.route('/movies')
def movies():
    return render_template('searchpage.html', title='Movies')

@app.route('/music')
def music():
    return render_template('searchpage.html', title='Music')

@app.route('/bugreport')
def bugreport():
    return render_template('bugReport.html', title='Bug Reports')
