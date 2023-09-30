from app import app # second app is variable app from __init__.py

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!" # Note that browser will convert
                           # string into html document
