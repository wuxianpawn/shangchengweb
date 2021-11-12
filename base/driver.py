from selenium import webdriver
import pageObject
from base.openDriver import OpenDriver

"""
单例模式：是一种设计思想
单例  表示一个类只能创建一个对象，一个是指所有创建的对象的内存地址都是一个，即：id（对象1）== id（对象2）
只能创建具有相对内存地址的对象
应用场景：回收站，任务管理器，日志，数据库连接池  
"""


class Driver:
    # 标记，用它来判断是否实例化过对象
    # 初始化，定义一下这个driver从来没有实例化过
    # 类属性 类方法是操作类属性的
    driver = None
    @classmethod
    def get_driver(cls):
        # 实例化driver对象  控制Chrome这个类只调用一次
        # 条件语句：判断一下driver属性是否被赋值过，即Chrome（）是否被实例化过
        if cls.driver is None:
            # cls.driver = webdriver.Chrome()
            cls.driver = OpenDriver().get_deriver('谷歌')
            cls.driver.get(pageObject.url)
            cls.driver.maximize_window()
        return cls.driver

    @classmethod
    def close_driver(cls):
        # 为了程序的健壮性，需要判断driver是否为None
        # 如果driver是存在的
        if cls.driver:
            cls.driver.quit()
            # 必须置空
            cls.driver = None
