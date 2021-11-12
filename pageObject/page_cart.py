import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pageObject
from base.baseApi import Base
"""
这里只做动作的组装和业务逻辑的组装
"""


class PageCart(Base):
    # 点击删除按钮
    @allure.step('点击删除按钮')
    def click_delect_button(self):
        # self.driver.find_element_by_xpath('//*[@data-value="粉色"]').click()
        self.base_click(pageObject.cart_delete_button)

    # 确认删除
    @allure.step('点击确定删除')
    def click_confirm_delect(self):
        self.base_click(pageObject.cart_confirm_delect)
