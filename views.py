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
    elif flag == 3 or flag == 4:
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
    results = send_and_get(command)
    return render_template('index.html', results=results)


def send_and_get(command):
    con = Connect()
    result = con.use_command(
                session['name'], session['host'], session['passwd'], command)
    return result


@app.route('/server_info')
def get_server_info():
    new_disk_info = []
    new_device_info = []
    new_ram_info = []
    ram_infos = []
    disk_infos = []
    device_infos = []

    con = Connect()
    serverInfo = con.server_info(
        session['name'], session['host'], session['passwd'])

    # ram info
    ram_info = serverInfo['ram_info']
    for i in range(1, len(ram_info)-1):
        new_ram_info.append(ram_info[i])
    for s in new_ram_info:
        one_info = s.strip('\n\t').split()
        ram_infos.append(one_info)
    ram_infos[1][1] = int(ram_infos[1][1]) / 1024
    ram_infos[1][2] = int(ram_infos[1][2]) / 1024
    ram_infos[1][3] = int(ram_infos[1][3]) / 1024

    # disk info
    disk_info = serverInfo['disk_info']
    for i in range(2, len(disk_info)-1):
        new_disk_info.append(disk_info[i])

    for s in new_disk_info:
        one_info = s.strip('\n\r').split()
        disk_infos.append(one_info)

    # device_info
    device_info = serverInfo['device_info']
    for i in range(1, len(device_info)-1):
        new_device_info.append(device_info[i])
    for s in new_device_info:
        device_infos = s.strip('\r\n').split()

    return render_template(
        'index.html',
        diskInfo=disk_infos, ramInfo=ram_infos, deviceInfo=device_infos)
