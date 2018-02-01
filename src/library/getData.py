import csv,os
from src.library.getPath import getTestDataPath

def getDataFromCsv(file):
    """读取csv文件"""
    all_test_data = []
    filepath=getTestDataPath()
    basepath=os.path.join(filepath,file)
    with open(basepath,'r',encoding='utf-8') as filedata:
        # print(filedata)
        filereader = csv.reader(filedata)
        # print(filereader)

        next(filereader)   # 去掉第一行列名数据
        for row in filereader:
            # print(row)
            all_test_data.append(row)

    return all_test_data


def getRegisterData():
    """读取项目中的csv文件"""
    file='register_testdata.csv'
    datas=getDataFromCsv(file)
    return datas


def getLoginData():
    """读取项目中的csv文件"""
    file='login_testdata.csv'
    datas=getDataFromCsv(file)
    return datas


def getPostData():
    """读取项目中的csv文件"""
    file='post_testdata.csv'
    datas=getDataFromCsv(file)
    return datas

login_data=getLoginData()
register_data=getRegisterData()
post_data=getPostData()

# print(login_data)
# print(register_data)
# print(post_data)







