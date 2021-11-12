import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pageObject
from base.baseApi import Base
"""
这里只做动作的组装和业务逻辑的组装
"""


class PageMyAddress(Base):
    # 点击新增地址的按钮
    @allure.step('点击新增地址的按钮')
    def click_new_address(self):
        self.base_click(pageObject.myaddress_add_address)

    # 切换iframe  通过index方式（索引的方式） 从0开始 目标iframe是index = 2 第三个iframe
    @allure.step('切换iframe-编辑我的地址页面')
    def switch_to_iframe(self):
        # 通过iframe的索引值定位
        self.base_switch_iframe(2)

    # 输入用户名
    @allure.step('输入用户名')
    def input_name(self):
        self.base_input(pageObject.myaddress_username, 'xiaopawn')

    # 输入电话
    @allure.step('输入电话')
    def input_tel(self):
        self.base_input(pageObject.myaddress_tel, '13845969564')

    @allure.step('选择省')
    def select_prov(self):
        # js让select框显示
        self.base_js(pageObject.myaddress_js_prov)
        # select 省 选择北京
        self.base_select_visible_text(pageObject.myaddress_prov, '北京市')
        time.sleep(2)

    @allure.step('选择市')
    def select_city(self):
        self.base_js(pageObject.myaddress_js_city)
        self.base_select_visible_text(pageObject.myaddress_city, '西城区')
        time.sleep(2)

    @allure.step('选择区')
    def select_country(self):
        self.base_js(pageObject.myaddress_js_country)
        self.base_select_visible_text(pageObject.myaddress_country, '德胜街道')
        time.sleep(2)

    # 输入详细地址
    @allure.step('输入详细地址')
    def detail_address(self):
        self.base_input(pageObject.myaddress_detailaddress, '德胜楼32号')

    # 输入别名
    @allure.step('输入别名')
    def name_nick(self):
        self.base_input(pageObject.myaddress_nickname, 'pawn')

    # 点击保存
    @allure.step('点击保存')
    def address_save(self):
        self.base_click(pageObject.myaddress_save)