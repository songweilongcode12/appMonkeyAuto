# python module for interacting with adb
import os
from loguru import logger
'''
基本的adb操作
'''
class AndroidDebugBridge(object):


    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        #logger.info(command_text)
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

    def get_app_packagename(self,filepath):
        packagesName =self.call_adb('aapt dump badging  %s %s'% filepath)
        return packagesName
    def install_app(self,filepath):
        self.call_adb(' -r install %s'% filepath)
    def unstall_app(self):
        self.call_adb('unstall %s'% self.get_app_packagename(self))
        # check for any fastboot device
    def fastboot(self, device_id):
        pass

    # 检查设备
    def attached_devices(self):
        result = self.call_adb("devices")
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        return [device for device in devices if len(device) > 2]

    """def attached_devices2(self):
        dev_list = []
        rt = os.popen('adb devices').readlines()  # os.popen()执行系统命令并返回执行后的结果
        n = len(rt) - 2
        # logger.info("当前已连接待测手机数为：" + str(n))
        for i in range(n):
            nPos = rt[i + 1].index("\t")
            dev = rt[i + 1][:nPos]
            dev_list.append(dev)

            logger.info("22222222222:",dev_list)
            flag = [device for device in dev_list if len(device) > 0]
            if flag:
                return True
            else:
                return False"""

    # 状态
    def get_state(self):
        result = self.call_adb("get-state")
        result = result.strip(' \t\n\r')
        return result or None
    #重启
    def reboot(self, option):
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery",):
            command = "%s %s" % (command, option.strip())
        self.call_adb(command)

    # 将电脑文件拷贝到手机里面
    def push(self, local, remote):
        result = self.call_adb("push %s %s" % (local, remote))
        return result

    # 拉数据到本地
    def pull(self, remote, local):
        result = self.call_adb("pull %s %s" % (remote, local))
        return result
    # 同步更新 很少用此命名
    def sync(self, directory, **kwargs):
        command = "sync %s" % directory
        if 'list' in kwargs:
            command += " -l"
            result = self.call_adb(command)
            return result

    # 打开指定app
    def open_app(self,packagename,activity,dev):
        result = self.call_adb("-s "+ dev+" shell am start -n %s/%s" % (packagename, activity))
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    # 根据包名得到进程id
    def get_app_pid(self, pkg_name):
        string = self.call_adb("shell ps | grep "+pkg_name)
        # logger.info(string)
        if string == '':
            return "the process doesn't exist."
        result = string.split(" ")
        # logger.info(result[4])
        return result[4]

def test_questios(new_list):
    a = new_list
    for i in a:
        indexs = a.index(i)
        max1 = a.index(min(a))
        logger.info(indexs)
        logger.error(max1)
        






test_questios(new_list=[1,2,3,4,5,6,7])
# if __name__ == '__main__':
#     AndroidDebugBridge.attached_devices()