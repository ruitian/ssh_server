# -*- coding: utf-8 -*-
import pexpect


class Connect():

    SERVER_INFO = {}

    def get_connect(self, name, host, passwd):
        cmd = 'ssh -t ' + name + '@' + host
        ssh = pexpect.spawn(cmd)
        flag = ssh.expect(
            ['password:', 'continue connecting (yes/no)?'], timeout=10)
        if flag == 0:
            ssh.sendline(passwd)
            flag2 = ssh.expect(
                ['password:', '~\$', '~#', pexpect.EOF, pexpect.TIMEOUT],
                timeout=5)
            return flag2

        elif flag == 1:
            ssh.sendline("yes\n")
            flag = 0

        return {
            'flag': flag
        }

    def use_command(self, name, host, passwd, cmd):
        new_cmd = 'ssh -t ' + name + '@' + host + ' ' + '"' + cmd + '"'
        ssh = pexpect.spawn(new_cmd)
        flag = ssh.expect(
            ['password:', 'continue connecting (yes/no)?'], timeout=10)
        if flag == 0:
            ssh.sendline(passwd)
        return ssh.readlines()

    def server_info(self, name, host, passwd):
        self.ram_info(name, host, passwd)
        self.disk_info(name, host, passwd)
        self.device_info(name, host, passwd)
        return self.SERVER_INFO

    def ram_info(self, name, host, passwd):
        cmd = 'ssh -t ' + name + '@' + host + ' ' + 'free'
        ssh = pexpect.spawn(cmd)
        flag = ssh.expect(['password:'], timeout=10)
        if flag == 0:
            ssh.sendline(passwd)
            self.SERVER_INFO['ram_info'] = ssh.readlines()

    def disk_info(self, name, host, passwd):
        cmd = 'ssh -t ' + name + '@' + host + ' ' + 'df -h'
        ssh = pexpect.spawn(cmd)
        flag = ssh.expect(['password:'], timeout=10)
        if flag == 0:
            ssh.sendline(passwd)
            self.SERVER_INFO['disk_info'] = ssh.readlines()

    def device_info(self, name, host, passwd):
        cmd = 'ssh -t ' + name + '@' + host + ' uptime'
        ssh = pexpect.spawn(cmd)
        flag = ssh.expect(['password:'], timeout=10)
        if flag == 0:
            ssh.sendline(passwd)
            self.SERVER_INFO['device_info'] = ssh.readlines()
