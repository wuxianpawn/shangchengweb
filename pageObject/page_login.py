import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pageObject
from base.baseApi import Base
"""
这里只做动作的组装和业务逻辑的组装
"""


class PageLogin(Base):
    # def __init__(self, driver):
    #     # 定义实例属性driver
    #     self.driver = driver

    # # 页面动作划分
    # # 在首页点击登陆按钮
    # def click_login_link(self):
    #     self.driver.find_element_by_link_text('登录').click()

    # 输入用户名
    @allure.step('输入用户名')
    def input_username(self, usename):

        self.base_input(pageObject.login_name, usename)
        # self.driver.find_element_by_name('accounts').send_keys('xiaopawn')

    # 输入密码
    @allure.step('输入密码')
    def input_pwd(self, password):

        self.base_input(pageObject.login_pwd, password)
        # self.driver.find_element_by_name('pwd').send_keys('123456')

    # 点击登录
    @allure.step('点击登录')
    def click_login_button(self):

        self.base_click(pageObject.login_button)
        # self.driver.find_element_by_xpath('//form/div[3]/button').click()

    # # 形成组合页面
    # def longin_business(self):
    #     # 依次调用
    #     # 点击登录链接
    #     self.click_login_link()
    #     # 输入用户名
    #     self.input_username()
    #     # 输入密码
    #     self.input_pwd()
    #     # 点击登录按钮
    #     self.click_login()

    # # 断言
    # def assert_login(self):
    #     time.sleep(3)
    #     if 'xiaopawn' in self.driver.page_source:
    #         print('登录成功')

    # # 退出浏览器
    # def close_driver(self):
    #     self.driver.close()

