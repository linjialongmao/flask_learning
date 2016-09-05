# coding = utf-8

from flask import Flask, render_template, session, url_for, redirect, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard '
bootstrap = Bootstrap(app)
manager = Manager(app)
CODEC = 'utf-8'

class NameForm(Form):
    name = StringField(u'请输入你的名字?')
    submit = SubmitField(u'提交')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name != None and old_name != form.name.data:
            flash(u'输入名字不一致，请重新输入')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', name=session.get('name'), form=form)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return  render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return  render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
