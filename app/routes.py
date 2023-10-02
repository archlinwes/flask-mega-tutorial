from flask import render_template
from app import app # second app is variable app from __init__.py

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Wesley'}
    return render_template('index.html', title='Home', user=user)
