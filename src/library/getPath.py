import os

# class getPath():
def get_root_path():
    """获得项目根路径"""
    rootpath = os.path.dirname(os.path.abspath(__file__))
    while rootpath:
        if os.path.exists(os.path.join(rootpath, 'readme.md')):
            break

        rootpath = rootpath[0:rootpath.rfind(os.path.sep)]
    # yield rootpath
    return rootpath

def getTestDataPath():
    """获得报告路径"""
    getTestDataPath=os.path.join(get_root_path(),'src','data')
    if not os.path.exists(getTestDataPath):
        os.mkdir(getTestDataPath)
    return getTestDataPath

def getScreenshotpath():
    """获得截图路径"""
    screenshotpath=os.path.join(get_root_path(),'src','screenshots')
    if not os.path.exists(screenshotpath):
        os.mkdir(screenshotpath)
    return screenshotpath


def getReportPath():
    """获得报告路径"""
    reportPath=os.path.join(get_root_path(),'src','report')
    if not os.path.exists(reportPath):
        os.mkdir(reportPath)
    return reportPath

def getCasePath():
    """获得报告路径"""
    casePath = os.path.join(get_root_path(), 'src', 'senarios')
    if not os.path.exists(casePath):
        os.mkdir(casePath)
    return casePath


#
# rootPath=get_root_path()
# print(rootPath)


# rootPath=getReportPath()
# print(rootPath)