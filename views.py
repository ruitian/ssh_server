# -*- coding: utf-8 -*-
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask import url_for
from flask import flash

from app import app
from ssh import Connect


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/connect', methods=['GET', 'POST'])
def connect():
    session['name'] = name = request.form['name']
    session['host'] = host = request.form['host']
    session['passwd'] = passwd = request.form['passwd']
    con = Connect()
    flag = con.get_connect(name, host, passwd)
    if flag == 0:
        flash(u'连接失败，请检查您的输入', 'danger')
        return redirect(url_for('deactive'))
    elif flag == -2 or flag == -1:
        flash(u'连接超时，请尝试重新连接', 'danger')
        return redirect(url_for('deactive'))
    else:
        return redirect(url_for('index'))


@app.route('/deactive', methods=['POST', 'GET'])
def deactive():
    if request.method == 'POST' or request.method == 'GET':
        session.pop('name')
        session.pop('host')
        session.pop('passwd')
        return redirect(url_for('index'))


@app.route('/<command>')
def send_cmd(command):
    pass


def send_and_get(command):
    pass
