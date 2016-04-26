# -*- coding: utf-8 -*-
from flask import render_template

from ssh import app

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
