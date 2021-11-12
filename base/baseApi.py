"""
三个业务都需要driver进行初始化，所以抽离出一个基类，也就是父类
api起的名字要见名知意
封装的是项目常用的api方法
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from tool.logger import GetLogger
log = GetLogger.get_logger()


class Base(object):
    def __init__(self, driver):
        log.info('正在初始化获取driver对象{}'.format(driver))
        self.driver = driver

    # 封装的目的：尽量用一个函数就可以全部封装，假如无法用一个方法，多个也行，只要合理就ok
    # 找元素方法的封装
    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        """
        usage:for example
        loc = By.CSS_SELECTOR, '#floor2 div.goods-list>div:nth-child(1)'
        :param loc:
        :return:
        """
        # 用显示等待做进一步的封装WebDriverWait().until(找元素的方法)
        # el = self.driver.find_element(*loc)
        log.info('正在查找元素：{}元素，最多等待{}秒'.format(loc, timeout))
        el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(lambda x: x.find_element(*loc))
        return el

    # 点击的封装
    def base_click(self, loc):
        log.info('正在点击：{}元素'.format(loc))
        # 找到元素
        # 点击
        self.base_find_element(loc).click()

    # 输入的封装（清空，输入）
    def base_input(self, loc, value):
        # 找到元素
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 切换窗口的封装
    def base_switch_window(self, title):
        """
        通过title进行切换
        :param title: 窗口的title
        :return:
        """
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                break

    # 切换iframe的封装
    # 好处：调用logger日志，可以把切换frame的这个动作记录到logger日志中
    def base_switch_iframe(self, frame):
        self.driver.switch_to.frame(frame)

    # 切回默认的iframe
    def base_default_ifarme(self, frame):
        self.driver.switch_to.defaule_content()

    # @property 加上这个就会把函数变成属性-前提是函数不需要传参
    @property
    def base_page_source(self):
        """
        返回页面源码
        主要作用是做断言
        :return:
        """
        return self.driver.page_source

    def base_js(self, script):
        self.driver.execute_script(script)
        log.info('正在查找到的元素是{}'.format(script))

    def base_select_visible_text(self, loc, text):
        # 先找到元素
        el = self.base_find_element(loc)
        # 实例化下拉框，获取select下拉框里面的option（列表数值）的值
        Select(el).select_by_visible_text(text)

    def base_click_index(self):
        """
        点击商城的首页
        :return:
        """
        click_url = By.CSS_SELECTOR, 'div#doc-topbar-collapse>ul>li:nth-child(1)>a'
        self.base_click(click_url)