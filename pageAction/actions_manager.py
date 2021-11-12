from pageObject.page_buy import PageBuy
from pageObject.page_cart import PageCart
from pageObject.page_goods_detail import PageGoodsDetail
from pageObject.page_index import PageIndex
from pageObject.page_login import PageLogin
from pageObject.page_myaddress import PageMyAddress
from pageObject.page_personcenter import PagePersonCenter


class ActionManager:
    """
    用于管理页面对象
    有多少个页面对象，就实例化多少个，然后其他业务就继承ActionManager这个类
    """
    def __init__(self, driver):
        self.pageindex = PageIndex(driver)
        self.pagelogin = PageLogin(driver)
        self.pagegoodstail = PageGoodsDetail(driver)
        self.pagebuy = PageBuy(driver)
        self.pagepersoncenter = PagePersonCenter(driver)
        self.pagemyaddress = PageMyAddress(driver)
        self.pagecart = PageCart(driver)
