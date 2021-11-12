import time

from base.baseApi import Base
from selenium.webdriver.support.select import Select
import pageObject
"""
这里只写业务和动作的业务组合
1、配置信息
2、页面步骤
3、组合业务
4、case
"""


class AddAddress(Base):
    # def __init__(self, driver):
    #     """
    #
    #     :param driver: 实例化好的对象
    #     """
    #     # 给对象赋予属性
    #     self.driver = driver

    # 点击个人中心
    def click_person_center(self):
        self.base_click(pageObject.index_person_center)

    # 点击我的地址
    def click_my_address(self):
        self.base_click(pageObject.personcenter_myaddress_link)

    # 点击新增地址的按钮
    def click_new_address(self):
        self.base_click(pageObject.myaddress_add_address)

    # 切换iframe  通过index方式（索引的方式） 从0开始 目标iframe是index = 2 第三个iframe
    def switch_to_iframe(self):
        # 通过iframe的索引值定位
        self.base_switch_iframe(2)

    # 输入用户名
    def input_name(self):
        self.base_input(pageObject.myaddress_username, 'xiaopawn')

    # 输入电话
    def input_tel(self):
        self.base_input(pageObject.myaddress_tel, '13845969564')

    def select_prov(self):
        # js让select框显示
        self.base_js(pageObject.myaddress_js_prov)
        # select 省 选择北京
        self.base_select_visible_text(pageObject.myaddress_prov, '北京市')
        time.sleep(2)

    def select_city(self):
        self.base_js(pageObject.myaddress_js_city)
        self.base_select_visible_text(pageObject.myaddress_city, '西城区')
        time.sleep(2)

    def select_country(self):
        self.base_js(pageObject.myaddress_js_country)
        self.base_select_visible_text(pageObject.myaddress_country, '德胜街道')
        time.sleep(2)

    # 输入详细地址
    def detail_address(self):
        self.base_input(pageObject.myaddress_detailaddress, '德胜楼32号')

    # 输入别名
    def name_nick(self):
        self.base_input(pageObject.myaddress_nickname, 'pawn')

    # 点击保存
    def address_save(self):
        self.base_click(pageObject.myaddress_save)


    # 组合业务
    def addaddress_business(self):
        self.click_person_center()
        self.click_my_address()
        self.click_new_address()
        self.switch_to_iframe()
        self.input_name()
        self.input_tel()
        self.input_prov_city_country()
        self.detail_address()
        self.name_nick()
        self.address_save()


if __name__ == '__main__':
    # 调用登录
    from web_login import Login
    # driver = webdriver.Chrome()
    # driver.get('http://121.42.15.146:9090/mtx/')
    from base.driver import Driver
    driver = Driver().get_driver()
    login = Login(driver)
    # 成功登录的方法
    login.longin_business()
    # 调用新增地址的业务
    AddAddress(driver).addaddress_business()
    time.sleep(1)
    assert '新增成功' in driver.page_source
