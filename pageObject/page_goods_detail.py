import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pageObject
from base.baseApi import Base
"""
这里只做动作的组装和业务逻辑的组装
"""


class PageGoodsDetail(Base):
    # 点击粉色
    @allure.step('点击粉色')
    def click_pink(self):
        # self.driver.find_element_by_xpath('//*[@data-value="粉色"]').click()
        self.base_click(pageObject.loc_pink)

    @allure.step('点击M码')
    # 点击M
    def click_M(self):
        # self.driver.find_element_by_xpath('//*[@data-value="M"]').click()
        self.base_click(pageObject.loc_M)

    @allure.step('点击立即购买')
    # 点击立即购买
    def click_buy_now(self):
        # self.driver.find_element_by_xpath('//*[text()= "立即购买"]').click()
        self.base_click(pageObject.loc_buy_now)

    # 点击加入购物车
    @allure.step('点击加入购物车')
    def click_add_cart(self):
        self.base_click(pageObject.goods_detail_add_cart)

    # 点击商品详情页的购物车
    @allure.step('点击右上角的购物车')
    def click_goods_right_cart(self):
        self.base_click(pageObject.goods_detail_click_right_cart)
