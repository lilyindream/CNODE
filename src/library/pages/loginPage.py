from selenium import webdriver
from selenium.webdriver.common.by import By
from src.library.pages.basePage import basePage
from time import sleep

class loginPage(basePage):
    """封装登录页面元素及操作"""
    cnode_login_button_loc = (By.XPATH, '/html/body/div[1]/div/div/ul/li[6]/a')

    def cnode_login(self):
        self.find_element(*self.cnode_login_button_loc).click()
        sleep(2)
        #assert等于登录页面


    #注册元素定位参数
    login_name_loc=(By.ID,'name')
    login_pwd_loc= (By.ID, 'pass')
    login_button_loc= (By.CLASS_NAME, 'span-primary')


    #登录用户名
    def login_name(self,username='lilytest'):
        self.find_element(*self.login_name_loc).send_keys(username)

    #登录用户密码
    def login_password(self,password='123451'):
        self.find_element(*self.login_pwd_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #定义统一入口
    def user_login(self,username='lilytest',password='123451'):
        self.cnode_login()
        self.login_name()
        self.login_password(password)
        self.login_button()
        sleep(3)

     #返回登录成功或失败提示信息

    rmessages_f = (By.XPATH, '//*[@id="content"]//strong')
    rmessages_s = (By.CLASS_NAME, 'dark')

    def rmessage_fail(self):
        return  self.find_element(self.rmessages_f).text

    def rmessage_pass(self):
        return  self.find_element(self.rmessages_s).text


dr=webdriver.Chrome('D:/PythonProject/CnodeTest/CNODE/chromedriver.exe')
dr.get('http://118.31.19.120:3000/')
loginPage(dr).user_login()


