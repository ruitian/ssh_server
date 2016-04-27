# -*- coding: utf-8 -*-
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask import url_for

from app import app
from ssh import Connect


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/result')
def result():
    return session['name']


@app.route('/connect', methods=['GET', 'POST'])
def connect():
    session['name'] = name = request.form['name']
    session['host'] = host = request.form['host']
    session['passwd'] = passwd = request.form['passwd']
    con = Connect()
    print con.get_connect(name, host, passwd)
    if con.get_connect(name, host, passwd) == 0:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('deactive'))


@app.route('/deactive', methods=['POST', 'GET'])
def deactive():
    if request.method == 'POST' or request.method == 'GET':
        session.pop('name')
        session.pop('host')
        session.pop('passwd')
        return redirect(url_for('index'))
