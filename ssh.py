# -*- coding: utf-8 -*-
import pexpect


class Connect():

    def get_connect(self, name, host, passwd):
        # cmd = 'ssh -t ' + name + '@' + host + ' ' + '"' + cmd + '"'
        cmd = 'ssh -t ' + name + '@' + host
        ssh = pexpect.spawn(cmd)
        try:
            flag = ssh.expect(
                ['password:', 'continue connecting (yes/no)?'], timeout=10)
            if flag == 0:
                ssh.sendline(passwd)
                flag2 = ssh.expect(['password:', '~#', '~$'])
                return flag2

            elif flag == 1:
                ssh.sendline("yes")
                flag = 0

            return {
                'flag': flag
            }
        except pexpect.EOF:
            print "EOF"
            ssh.close()
            ret = -1
        except pexpect.TIMEOUT:
            print "TIMEOUT"
            ssh.close()
            ret = -2
        return ret
