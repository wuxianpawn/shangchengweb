import time

from base.driver import Driver
from pageAction.actions_manager import ActionManager
from pageObject.page_index import PageIndex
from pageObject.page_login import PageLogin
"""
第一种方法：在登录这个类中进行两个页面的实例化
第二种方法：多继承
"""


# 简单的写法
class Login(ActionManager):
    """
组合业务
登录业务需要哪几个页面的哪几个步骤？
1、登录页面  3个步骤
2、index页面 1个步骤
    """
    # 组合业务：成功的业务
    def login_success(self):
        # 点击首页的登录链接
        self.pageindex.click_login_link()
        # 输入用户名
        self.pagelogin.input_username('xiaopawn')
        # 输入密码
        self.pagelogin.input_pwd('123456')
        # 点击登录
        self.pagelogin.click_login_button()
        time.sleep(3)

    # 组合业务：登录的业务（参数化）
    def login_business(self, username, password):
        # 点击首页的登录链接
        self.pageindex.click_login_link()
        # 输入用户名
        self.pagelogin.input_username(username)
        # 输入密码
        self.pagelogin.input_pwd(password)
        # 点击登录
        self.pagelogin.click_login_button()
        time.sleep(3)

# 继承的写法
# class Login1(PageIndex, PageLogin):
#     """
# 组合业务
# 登录业务需要哪几个页面的哪几个步骤？
# 1、登录页面  3个步骤
# 2、index页面 1个步骤
#     """
#     # 组合业务：成功的业务
#     def login_success(self):
#         # 点击首页的登录链接
#         self.pageindex.click_login_link()
#         # 输入用户名
#         self.pagelogin.input_username('xiaopawn')
#         # 输入密码
#         self.pagelogin.input_pwd('123456')
#         # 点击登录
#         self.pagelogin.click_login_button()
#
#     # 组合业务：登录的业务（参数化）
#     def login_business(self, username, password):
#         # 点击首页的登录链接
#         self.pageindex.click_login_link()
#         # 输入用户名
#         self.pagelogin.input_username(username)
#         # 输入密码
#         self.pagelogin.input_pwd(password)
#         # 点击登录
#         self.pagelogin.click_login_button()
#
# # 普通写法
# class Login2(object):
#     """
# 组合业务
# 登录业务需要哪几个页面的哪几个步骤？
# 1、登录页面  3个步骤
# 2、index页面 1个步骤
#     """
#     def __init__(self, driver):
#         """
#         1、实例化页面对象
#         2、调用页面对象里面的步骤
#         :param driver:
#         """
#         self.pagelogin = PageLogin(driver)
#         self.pageindex = PageIndex(driver)
#
#     # 组合业务：成功的业务
#     def login_success(self):
#         # 点击首页的登录链接
#         self.pageindex.click_login_link()
#         # 输入用户名
#         self.pagelogin.input_username('xiaopawn')
#         # 输入密码
#         self.pagelogin.input_pwd('123456')
#         # 点击登录
#         self.pagelogin.click_login_button()
#
#     # 组合业务：登录的业务（参数化）
#     def login_business(self, username, password):
#         # 点击首页的登录链接
#         self.pageindex.click_login_link()
#         # 输入用户名
#         self.pagelogin.input_username(username)
#         # 输入密码
#         self.pagelogin.input_pwd(password)
#         # 点击登录
#         self.pagelogin.click_login_button()


if __name__ == '__main__':
    driver = Driver.get_driver()
    Login(driver).login_success()
