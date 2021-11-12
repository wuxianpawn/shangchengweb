import time

import allure

import pageObject
from base.baseApi import Base
from base.driver import Driver
from pageAction.cart_action import Cart
from pageAction.login_action import Login
"""
case
测试用例（N条）
需要知道起始点在哪里
原则：1、需要做保证起始动作都在相同的页面--相同页面就是首页
      2、目的：回到首页
      2.1、一个测试用例结束的时候 点击index标签---回到首页
      解决办法：销毁函数，teardown_method()
      2.2、后一个测试用例开始的时候，get（url）setup_method()
"""


@allure.feature('购物车功能的测试')
class TestCart(object):
    def setup_class(self):
        # 创建driver对象
        self.driver = Driver.get_driver()
        # 依赖登录，调用成功登录的业务
        Login(self.driver).login_success()
        # 创建cart对象
        self.cart = Cart(self.driver)
        # 实例化一个base对象
        self.base = Base(self.driver)

    # 关闭driver
    def teardown_class(self):
        Driver.close_driver()

    # 第一种办法：销毁函数---点击index首页
    def teardown_method(self):
        self.base.base_click_index()
    # # 第二种办法：初始化函数----get（url）
    # def setup_method(self):
    #     self.driver.get(pageObject.url)

    # 测试用例:添加购物车
    @allure.title('添加购物车测试用例')
    def test_add(self):
        self.cart.business_add_cart()
        time.sleep(3)
        assert '加入成功' in self.base.base_page_source

    # 删除购物车
    @allure.title('删除购物车的测试用例')
    def test_delect(self):
        self.cart.business_delect_cart()
        time.sleep(3)
        assert '删除成功' in self.base.base_page_source
