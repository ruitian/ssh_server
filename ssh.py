# -*- coding: utf-8 -*-
import pexpect


class Connect():

    def get_connect(self, name, host, passwd):

        cmd = 'ssh -t ' + name + '@' + host
        ssh = pexpect.spawn(cmd)
        try:
            flag = ssh.expect(
                ['password:', 'continue connecting (yes/no)?'], timeout=5)
            if flag == 0:
                pexpect.run(cmd, events={'password:': passwd}, timeout=2)
            elif flag == 1:
                ssh.sendline('yes')
                flag = 0
            return ssh
        except pexpect.EOF:
            print "EOF"
            ssh.close()
            ret = -1
        except pexpect.TIMEOUT:
            print "TIMEOUT"
            ssh.close()
            ret = -2
        return ret

    def send_cmd(self, name, host, passwd, cmd):
        ssh = self.get_connect(name, host, passwd)
        result = pexpect.run(cmd)
        ssh.close()
        return result
