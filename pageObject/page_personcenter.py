import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pageObject
from base.baseApi import Base
"""
这里只做动作的组装和业务逻辑的组装
"""


class PagePersonCenter(Base):
    # 点击我的地址
    @allure.step('点击我的地址')
    def click_my_address(self):
        self.base_click(pageObject.personcenter_myaddress_link)
