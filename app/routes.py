from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Michael'}
    posts = [
        {
            'author' : {'username': 'Michael'},
            'body' : 'Beautiful day in NYC'},
        {
            'author' : {'username' : 'Susan'},
            'body' : 'The Avengers movie was so cool!'},
        ]
    return render_template('index.html', title='Home', user=user, posts=posts)
