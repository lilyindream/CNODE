from time import sleep
import unittest,sys
from src.library.pages.loginPage import loginPage
from src.library.myUnit import baseTest
from src.library.getData import login_data
from src.library import myUnit

class  LoginCases(myUnit.baseTest):
    """cnode登录测试"""

    def test_login01(self):
        """正确的默认用户名密码登录"""

        loginPage(self.driver).user_login()
        # public.assertequal(loginout().rmessage_pass(),login_data[0][4])



if __name__ == '__main__':
    unittest.main()