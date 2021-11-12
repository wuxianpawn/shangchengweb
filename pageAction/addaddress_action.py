from pageAction.actions_manager import ActionManager


class AddAddress(ActionManager):
    def addaddress_business(self):
        self.pageindex.click_person_center()
        self.pagepersoncenter.click_my_address()
        self.pagemyaddress.click_new_address()
        self.pagemyaddress.switch_to_iframe()
        self.pagemyaddress.input_name()
        self.pagemyaddress.input_tel()
        self.pagemyaddress.select_prov()
        self.pagemyaddress.select_city()
        self.pagemyaddress.select_country()
        self.pagemyaddress.detail_address()
        self.pagemyaddress.name_nick()
        self.pagemyaddress.address_save()
