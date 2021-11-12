import time

import allure

from base.baseApi import Base
from base.driver import Driver
from pageAction.login_action import Login
from pageAction.addaddress_action import AddAddress


@allure.feature('新增地址的测试')
class TestAddAddress(object):
    def setup_class(self):
        # 创建driver对象
        self.driver = Driver.get_driver()
        # 依赖登录，调用成功登录的业务
        Login(self.driver).login_success()
        # 创建新增地址的对象
        self.addaddress = AddAddress(self.driver)
        # 实例化一个base对象
        self.base = Base(self.driver)

    # 关闭driver
    def teardown_class(self):
        Driver.close_driver()

    # 测试用例，新增地址
    @allure.title('新增地址的正向测试用例')
    def test_addaddress(self):
        # 调用新增地址成功的业务
        self.addaddress.addaddress_business()
        # 断言
        time.sleep(2)
        assert '新增成功' in self.base.base_page_source
