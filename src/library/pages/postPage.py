from selenium.webdriver.common.by import By
from src.library.pages.basePage import basePage
from time import sleep

class post(basePage):
    """用户发帖页面"""

    #发帖元素定位参数
    post_publish=(By.LINK_TEXT,'发布话题')
    post_title = (By.CSS_SELECTOR, '#title')
    post_content=(By.CSS_SELECTOR,'#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll')

    def posta(self,tab,title,content):
        if tab=='fenxiag' or tab== "分享":
            post_tab = (By.XPATH, '//*[@id="tab-value"]/option[2]')
        elif tab=='问答' or tab=='wenda':
            post_tab = (By.XPATH, '//*[@id="tab-value"]/option[3]')
        elif tab=='招聘' or  tab=='zhaopin':
            post_tab = (By.XPATH, '//*[@id="tab-value"]/option[4]')

        self.find_element(self.post_publish).click()
        sleep(3)
        self.find_element(self.post_tab).click()
        self.find_element(self.post_title).send_keys(title)
        drx=self.find_element(self.post_content)
        basePage().mouseMove(self,drx)
        sleep(3)


    uploadImageIcon = (By.CLASS_NAME, 'eicon-image')
    uploadInameInput=(By.CLASS_NAME, 'webuploader-element-invisible')

    def uploadImage(self):

        drs=self.find_element(self.uploadImageIcon).click()
        drs.click()
        dri=self.find_element(self.uploadInameInput).send_keys('D:\\cnode_test\\src\\interpreter.png')


    submitBtn=(By.XPATH,'//*[@id="create_topic_form"]/fieldset/div/div/div[4]/input')

    def  clickPostSubmit(self):
        drs=self.find_element(self.submitBtn)
        basePage().mouseMove(self,drs)
        sleep(3)
        drs.click()

    def find_latest_post(self):
        pass




    def delete_post(self):
        pass


     #返回登录成功或失败提示信息
    #
    # rmessages_f = (By.XPATH, '//*[@id="content"]//strong')
    # rmessages_s = (By.CLASS_NAME, 'dark')
    #
    # def rmessage_fail(self):
    #     return  self.find_element(self.rmessages_f).text
    #
    # def rmessage_pass(self):
    #     return  self.find_element(self.rmessages_s).text



