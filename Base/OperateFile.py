
import os
from loguru import logger
class base_file:
    #method(r,w,a)
    def __init__(self, file, method='w+'):
        self.file = file
        self.method = method
        self.fileHandle = None

    def write_txt(self, line):
        base_file(self.file).check_file()
        self.fileHandle = open(self.file, self.method)
        self.fileHandle.write(line + "\n")
        self.fileHandle.close()

    def read_txt_row(self):
        base_file(self.file).check_file()
        self.fileHandle = open(self.file, self.method)
        logger.info(self.fileHandle.readline())
        self.fileHandle.close()

    def read_txt_rows(self):
        base_file(self.file).check_file()
        self.fileHandle = open(self.file, self.method)
        file_list = self.fileHandle.readlines()
        for i in file_list:
            logger.info(i.strip("\n"))
        self.fileHandle.close()
    def check_file(self):
        if not os.path.isfile(self.file):
            # logger.info('文件不存在' + self.file)
            # sys.exit()
            return False
        else:
            return True
        # logger.info("文件存在！")

    def mkdir_file(self):
        if not os.path.isfile(self.file):
            f = open(self.file, self.method)
            f.close()
            logger.info("创建文件成功")
            return True
        else:
            logger.info("文件已经存在")
            return False
    def remove_file(self):
        if os.path.isfile(self.file):
            os.remove(self.file)
            logger.info("删除文件成功")
        else:
            logger.info("文件不存在")
if __name__ == '__main__':
    bf = base_file("text.xml")
    if bf.check_file() == False:
        bf.mkdir_file()
    bf.write_txt("111")