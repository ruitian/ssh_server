# -*- coding: utf-8 -*-
from flask import render_template
from flask import request

from app import app
from ssh import Connect

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        con = Connect()
        name = request.form['name']
        host = request.form['host']
        passwd = request.form['passwd']
        cmd = request.form['cmd']
        result = con.send_cmd(name, host, passwd, cmd)
        return render_template('index.html', result=result)
    return render_template('index.html')
