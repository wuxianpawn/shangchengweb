import time

from pageAction.actions_manager import ActionManager


class Order(ActionManager):
    # 组合业务：提交订单，并提示提交成功(断言)
    def business_order(self):
        self.pageindex.click_zk_skirt()
        self.pageindex.switch_widow()
        time.sleep(1)
        self.pagegoodstail.click_pink()
        time.sleep(2)
        self.pagegoodstail.click_M()
        time.sleep(2)
        self.pagegoodstail.click_buy_now()
        self.pagebuy.click_payment()
        self.pagebuy.click_submit_order()


if __name__ == '__main__':
    pass
