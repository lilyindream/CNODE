import unittest
from src.library.publicMethod import openBrower,openMainPage,caturing

class baseTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """打开浏览器"""
        self.dr=openBrower()
        #最大化浏览器窗口
        self.dr.maximize_window()
        #打开Cnode首页
        openMainPage(self.dr)



    @classmethod
    def tearDownClass(self):
        self.dr.quit()


    def setUp(self):
        pass

    def tearDown(self):
        caturing(self.dr)


if __name__ == '__main__':
    unittest.main()
