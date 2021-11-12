import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pageObject
from base.baseApi import Base
"""
这里只做动作的组装和业务逻辑的组装
"""


class PageBuy(Base):
    @allure.step('点击支付方式')
    # 点击支付方式
    def click_payment(self):
        # self.driver.find_element_by_xpath('//*[text()= "货到付款"]').click()
        self.base_click(pageObject.loc_payment)

    @allure.step('点击提交订单')
    # 点击提交订单
    def click_submit_order(self):
        # self.driver.find_element_by_xpath('//*[text()= "提交订单"]').click()
        self.base_click(pageObject.loc_submit_order)