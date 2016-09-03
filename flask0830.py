from flask import Flask
from flask.ext.script import Manager


app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def index(name):
    return '<h1>Hello %s!</h1>' % name


if __name__ == '__main__':
    manager.run()
