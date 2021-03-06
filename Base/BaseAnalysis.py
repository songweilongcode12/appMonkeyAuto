import math
from loguru import logger

# total 是rom容量
def avgMen(men, total):
    if len(men):
        _men = [math.ceil(((men[i]) / total) * 1024) for i in range(len(men))]
        logger.info(_men)
        return str(math.ceil(sum(_men) / len(_men))) + "M"
    return "0"


def avgCpu(cpu):
    if len(cpu):
        resutl = "%.1f" % (sum(cpu) / len(cpu))
        return str(math.ceil(float(resutl)*10)) + "%"
    return "0%"


def avgFps(fps):
    if len(fps):
        return '%.1f' % float(str(math.ceil(sum(fps) / len(fps))))
    return 0.0


def maxMen(men):
    if len(men):
        logger.info("men=" + str(men))
        return str(math.ceil((max(men)) / 1024)) + "M"
    return "0"


def maxCpu(cpu):
    logger.info("maxCpu="+str(cpu))
    if len(cpu):
        result = "%.1f" % max(cpu)
        return str(math.ceil(float(result)*10)) + "%"
    return "0%"


def maxFps(fps):
    if len(fps):
      return '%.1f' % float(max(fps))
    return 0.0


def maxFlow(flow):
    logger.info("---maxFlow111----------")
    logger.info(flow)
    _flowUp = []
    _flowDown = []
    for i in range(len(flow[0])):
        if i + 1 == len(flow[0]):
            break
        _flowUp.append(math.ceil((flow[0][i + 1] - flow[0][i]) / 1024))
        #logger.info("---maxFlow2222---------")
        #logger.info(_flowUp)
    for i in range(len(flow[1])):
        if i + 1 == len(flow[1]):
            break
        _flowDown.append(math.ceil((flow[1][i + 1] - flow[1][i]) / 1024))
        #logger.info("---maxFlow3333---------")
        #logger.info(_flowDown)
    if _flowUp:
        maxFpsUp = str(max(_flowUp)) + "KB"  # 上行流量
    else:
        maxFpsUp = "0"
    if _flowDown:
        maxFpsDown = str(max(_flowDown)) + "KB"  # 下行流量
    else:
        maxFpsDown = "0"
    return maxFpsUp, maxFpsDown

def avgFlow(flow):
    _flowUp = []
    _flowDown = []
    for i in range(len(flow[0])):
        if i + 1 == len(flow[0]):
            break
        _flowUp.append((flow[0][i + 1] - flow[0][i])/1024)

    for i in range(len(flow[1])):
        if i + 1 == len(flow[1]):
            break
        _flowDown.append((flow[1][i + 1] - flow[1][i])/1024)
    avgFpsUp = str(math.ceil(sum(_flowUp) / len(_flowUp))) + "KB"
    avgFpsDown = str(math.ceil(sum(_flowDown) / len(_flowDown))) + "KB"
    return avgFpsUp, avgFpsDown

