from selenium.webdriver.common.by import By
from src.library.pages.basePage import basePage
from time import sleep

class Register(basePage):
    """用户注册页面"""

    #注册元素定位参数
    register_name=(By.ID,'loginname')
    register_pwd = (By.ID, 'pass')
    register_repwd = (By.ID, 're_pass')
    register_mail = (By.ID, 'email')
    register_button = (By.CLASS_NAME, 'span-primary')

    def cnode_register(self,repassword,maila,username,password):
        self.find_element(self.register_name).send_keys(username)
        self.find_element(self.register_pwd).send_keys(password)
        self.find_element(self.register_repwd).send_keys(repassword)
        self.find_element(self.register_mail).send_keys(maila)
        self.find_element(self.register_button).click()
        sleep(3)

     #返回注册成功或失败提示信息

    rmessages = (By.XPATH, '//*[@id="content"]//strong')

    def rmessage(self):
         return self.find_element(self.rmessages).text



