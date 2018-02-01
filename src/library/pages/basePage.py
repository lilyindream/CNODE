from src.library import publicMethod
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep



class basePage(object):
    """页面基础类，用于所有页面的继承"""

    cnode_url='http://118.31.19.120:3000/'

    def __init__(self,driver,base_url=cnode_url):
        self.base_url=base_url
        self.driver=driver
        self.timeout='30'


    def open_page(self):
        self.driver.get(self.base_url)
        publicMethod.assertequal(self.driver.current_url,self.cnode_url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def jscript(self,js):
        return self.driver.execute(js)

    def mouseMove(self,driver,area):
        return ActionChains(driver).move_to_element(area).send_keys(Keys.CONTROL,'b').send_keys(Keys.CONTROL,'XXXX').perform()





