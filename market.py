from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about/<username>')
def about_page(username):
    return f'<h1>Pagina di {username}</h1>'


@app.route('/hello')
def hello_world():
    return '<h1>Hello World</h1>'

