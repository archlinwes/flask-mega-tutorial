from flask import render_template
from app import app # second app is variable app from __init__.py
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Wesley'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
