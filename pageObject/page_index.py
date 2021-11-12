import allure

import pageObject
from base.baseApi import Base


class PageIndex(Base):
    @allure.step('在首页点击登录链接')
    def click_login_link(self):
        self.base_click(pageObject.index_login_link)

    # 在首页点击zk裙子
    @allure.step('在首页点击zk裙子')
    def click_zk_skirt(self):
        self.base_click(pageObject.loc_zk_skirt)

    # 切换窗口（过渡的动作-前移-写在触发这个动作的页面上）
    @allure.step('切换窗口-首页至商品页')
    def switch_widow(self):
        self.base_switch_window(pageObject.title1)

    # 点击个人中心
    @allure.step('点击个人中心')
    def click_person_center(self):
        self.base_click(pageObject.index_person_center)

    # 点击购物车
    @allure.step('点击首页右上角购物车')
    def click_right_cart(self):
        self.base_click(pageObject.goods_detail_click_right_cart)
