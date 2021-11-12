from selenium.webdriver.common.by import By
"""
整个项目的配置项
"""
url = 'http://121.42.15.146:9090/mtx/'

"""以下是首页点击登录的配置信息"""
index_login_link = By.LINK_TEXT, '登录'
index_person_center = By.XPATH, '//*[text()="个人中心"]'
index_click_right_cart = By.XPATH, '(//*[text()="购物车"])[2]'
index_click_index = By.CSS_SELECTOR, 'div#doc-topbar-collapse>ul>li:nth-child(1)>a'

"""以下是登录页面的配置信息"""
login_name = By.NAME, 'accounts'
login_pwd = By.NAME, 'pwd'
login_button = By.XPATH, '//form/div[3]/button'

"""以下是个人中心的配置信息"""
personcenter_myaddress_link = By.LINK_TEXT, '我的地址'

"""以下是购物车的配置信息"""
cart_delete_button = By.XPATH, '(//*[text()="删除"])[1]'
cart_confirm_delect = By.XPATH, '//*[text()="确定"]'

"""以下是商品详情页的配置"""
goods_detail_add_cart = By.XPATH, '//*[text()="加入购物车"]'
loc_zk_skirt = By.CSS_SELECTOR, '#floor2 div.goods-list>div:nth-child(1)'
title1 = 'zk爆款连衣裙'
loc_pink = By.XPATH, '//*[@data-value="粉色"]'
loc_M = By.XPATH, '//*[@data-value="M"]'
loc_buy_now = By.XPATH, '//*[text()= "立即购买"]'
goods_detail_click_right_cart = By.XPATH, '//*[text()="购物车"]'

"""以下是新增地址的配置信息"""
myaddress_add_address = By.XPATH, '//*[text()="新增地址"]'
myaddress_username = By.NAME, 'name'
myaddress_tel = By.NAME, 'tel'
myaddress_prov = By.NAME, 'province'
myaddress_city = By.NAME, 'city'
myaddress_country = By.NAME, 'county'
myaddress_js_prov = "document.querySelectorAll('select')[0].style.display = 'inline'"
myaddress_js_city = "document.querySelectorAll('select')[1].style.display = 'inline'"
myaddress_js_country = "document.querySelectorAll('select')[2].style.display = 'inline'"
myaddress_detailaddress = By.NAME, 'address'
myaddress_nickname = By.NAME, 'alia'
myaddress_save = By.XPATH, '//*[text()="保存"'


"""下单功能的配置"""
loc_payment = By.XPATH, '//*[text()= "货到付款"]'
loc_submit_order = By.XPATH, '//*[text()= "提交订单"]'

