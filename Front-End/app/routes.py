from flask import render_template, request
from app import app
from app.forms import SearchForm
import requests

def process_input(data):
    if data != None:
        query_string = {"keyword": [], "username": ""}
        split_s = []
        s = data.split(", ")
        for i in s:
            split_s.append(i.replace(":", "").split(" "))
        for j in split_s:
            if j[0].lower() in query_string:
                if j[0].lower() == "keyword":
                    query_string["keyword"].append(j[1])
                if j[0].lower() == "username":
                    if query_string["username"] == "":
                        query_string["username"] = j[1]
            if j[0].lower() == "verified":
                if j[1].lower() == "true":
                    query_string["verified"] = "true"
            if j[0].lower() == "retweet":
                if j[1].lower() == "true":
                    query_string["retweet"] = "true"
        return query_string

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/sports', methods=['GET', 'POST'])
def sports():
    form = SearchForm(request.form)
    params = process_input(form.search_queries.data)
    if form.search_queries.data != None:
        requests.get("http://127.0.0.1:5000/search/sports", params=params)
    return render_template('searchpage.html', form=form, title='Sports')

@app.route('/movies', methods=['GET', 'POST'])
def movies():
    form = SearchForm(request.form)
    params = process_input(form.search_queries.data)
    if form.search_queries.data != None:
        requests.get("http://127.0.0.1:5000/search/movies", params=params)
    return render_template('searchpage.html', form=form, title='Movies')

@app.route('/music', methods=['GET', 'POST'])
def music():
    form = SearchForm(request.form)
    params = process_input(form.search_queries.data)
    if form.search_queries.data != None:
        requests.get("http://127.0.0.1:5000/search/music", params=params)
    return render_template('searchpage.html', form=form, title='Music')

@app.route('/bugreport')
def bugreport():
    return render_template('bugReport.html', title='Bug Reports')

# create another route for the forms to go to
    # query to url that api.py has