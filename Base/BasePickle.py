
import pickle
import os
from loguru import logger

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def writeSum(init, data=None, path="data.pickle"):
    if init == 0:
        result = data
    else:
        _read = readInfo(path)
        result = _read - 1

    with open(path, 'wb') as f:
        logger.info("------writeSum-------")
        logger.info(result)
        pickle.dump(result, f)


def readSum(path):
    data = {}
    with open(path, 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = {}
            logger.info("读取文件错误,文件内容为空")
    logger.info("------read-------")
    logger.info(path)
    logger.info(data)
    return data


def readInfo(path):
    data = []
    with open(path, 'rb') as f:
        try:
            data = pickle.load(f)
            # logger.info(data)
        except EOFError:
            data = []
            logger.info("读取文件错误,文件内容为空")
    logger.info("------read-------")
    logger.info(path)
    logger.info(data)
    return data


def writeInfo(data, path="data.pickle"):
    _read = readInfo(path)
    result = []
    if _read:
        _read.append(data)
        result = _read
    else:
        result.append(data)
    with open(path, 'wb') as f:
        logger.info("------writeInfo-------")
        logger.info(result)
        pickle.dump(result, f)

def writeFlowInfo(upflow, downflow, path="data.pickle"):
    #logger.info("---data-----")
    #logger.info("上行流量="+str(upflow))
    #logger.info("下行流量="+str(downflow))

    _read = readInfo(path)
    result = [[], []]
    if _read:
        _read[0].append(upflow)
        _read[1].append(downflow)
        result = _read
    else:
        result[0].append(upflow)
        result[1].append(downflow)
    with open(path, 'wb') as f:
        logger.info("------writeFlowInfo-------")
        logger.info(result)
        pickle.dump(result, f)


#if __name__ == "__main__":
    # readInfo(PATH("../info/DU2TAN15AJ049163_battery.pickle"))
    # readInfo(PATH("../info/emulator-5554_fps.pickle"))
    # readInfo(PATH("../info/emulator-5554_battery.pickle"))
    # readInfo(PATH("../info/emulator-5554_men.pickle"))
    # readInfo(PATH("../info/DU2TAN15AJ049163_men.pickle"))
    # readInfo(PATH("../info/emulator-5554_flow.pickle"))
    #readInfo("E:\\app\\py\\monkey1\\info\\info.pickle")
    # readInfo(PATH("../info/DU2TAN15AJ049163_cpu.pickle"))
