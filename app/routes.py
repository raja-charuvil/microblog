from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'raja'}
    posts = [
            {
                'author': {'username': 'John'},
                'body': 'Beautiful day in Kerala'
            },
            {
                'author': {'username': 'Susan'},
                'body': 'The climate is not so good here'
            }
            ]
    return render_template('index.html', title='Home', user=user, posts=posts)
