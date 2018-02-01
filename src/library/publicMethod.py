from src.library.getPath import get_root_path,getScreenshotpath
from pymongo import MongoClient
from selenium import webdriver

import time,os

def formatdate():
    return  time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

def assertequal(dr,message,predictinfo,casename):
    """assert是否实际提示和预期是否相等"""
    try:
        dr.assertEqual(message, predictinfo)
        print(casename+'：Test Pass')
        # print('预期提示:',data[6])
        # print('实际提示:', message)
    except Exception as e:
        print('页面提示信息和预期不一致:fail')
        # print('预期提示:',data[6])
        # print('实际提示:', message)
        raise AssertionError(casename+':Test Fail', format(e))


def assertin(dr,message,predictinfo,casename):
    """assert是否实际提示是否包含预期"""
    try:
        dr.assertIn(predictinfo,message)
        # print('页面提示信息和预期一致: pass')
        # print('预期提示:',data[6])
        # print('实际提示:', message)
    except Exception as e:
        # print('页面提示信息和预期不一致:fail')
        # print('预期提示:',data[6])
        # print('实际提示:', message)
        raise AssertionError(casename+':Test Fail:页面提示信息和预期不一致.', format(e))


def browerSelect(bro):
    """选择并打开浏览器"""
    if bro == 'chrome':
        driver = webdriver.Chrome(executable_path=get_root_path() + '/chromedriver.exe')
    elif bro == 'firefox':
        driver = webdriver.Firefox()
    elif bro == 'ie':
        driver = webdriver.Ie()
    return driver

def openBrower(bro='chrome'):
    dr = browerSelect(bro)
    return dr

def openMainPage(dr,url='http://118.31.19.120:3000/'):
    """打开Cnode首页"""
    dr.get(url)





def caturing(dr):
    """截图存并放到screenshot中"""
    dr.get_screenshot_as_file(os.path.join(getScreenshotpath(), 'screenshot'+formatdate() + ".png"))


def activeuser(usename):
    """激活注册的账号"""
    client = MongoClient('mongodb://118.31.19.120:27017/')
    print(client.database_names)
    db = client.get_database('node_club_dev')
    collections = db.collection_names()
    print(collections)
    users = db.get_collection('users')
    print(users)
    users.find_one_and_update({"loginname": usename}, {'$set': {"active": True}})


# print(os.path.join(getScreenshotpath(), 'screenshot'+formatdate() + ".png"))