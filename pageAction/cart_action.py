import time

from pageAction.actions_manager import ActionManager


class Cart(ActionManager):
    # 组合业务：添加购物车
    def business_add_cart(self):
        self.pageindex.click_zk_skirt()
        self.pageindex.switch_widow()
        self.pagegoodstail.click_pink()
        time.sleep(2)
        self.pagegoodstail.click_M()
        time.sleep(2)
        self.pagegoodstail.click_add_cart()

    # 组合业务：删除购物车
    def business_delect_cart(self):
        """
        删除商品之前要确保购物车有商品
        1、action层，先调用添加购物车这个业务（确保购物车里面有商品），再调用删除购物车业务
        1.1、需要动作能关联上
        2、case层，调整顺序，通过插件去用，不建议用，因为测试用例和测试用例之间是相互独立的，插件pytest-ordering
        :return:
        """
        # 调用当前类里的函数，直接self.函数
        # 调用添加业务
        self.business_add_cart()
        time.sleep(2)
        # 调用删除业务
        # 点击商品详情页右上角购物车
        self.pagegoodstail.click_goods_right_cart()
        # 点击购物车里的删除按钮
        self.pagecart.click_delect_button()
        # 点击确定
        self.pagecart.click_confirm_delect()

    def click_index(self):
        pass


if __name__ == '__main__':
    pass
