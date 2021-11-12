import time

import allure

from base.baseApi import Base
from base.driver import Driver
from pageAction.login_action import Login
from pageAction.order_action import Order


@allure.feature('下订单功能的测试')
class TestOrder(object):
    def setup_class(self):
        # 创建driver对象
        self.driver = Driver.get_driver()
        # 依赖登录，调用成功登录的业务
        Login(self.driver).login_success()
        # 创建order对象
        self.order = Order(self.driver)
        # 实例化一个base对象
        self.base = Base(self.driver)

    # 关闭driver
    def teardown_class(self):
        Driver.close_driver()

    # 测试用例，下订单
    @allure.title('下订单的正向测试用例')
    def test_order(self):
        # 调用下订单的业务
        self.order.business_order()
        # 断言
        time.sleep(2)
        assert '提交成功' in self.base.base_page_source