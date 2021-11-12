from selenium import webdriver


class OpenDriver(object):
    def get_deriver(self, browser):
        """
        对具体创建哪一个浏览器deriver的封装
        :param browser:浏览器的名字，比如ie，火狐，谷歌
        :return:指定浏览器的driver对象
        """
        if browser == 'firefox' or browser == 'ff':
            driver = webdriver.Firefox()
            return driver
        elif browser == 'chrome' or browser == 'ch' or browser == '谷歌':
            driver = webdriver.Chrome()
            return driver
        elif browser == 'ie' or browser == 'ff':
            driver = webdriver.Ie()
            return driver
        elif browser == '360':
            driver = webdriver.Ie
            return driver
        else:
            raise NameError('Not found {} such browser，make sure you enter correct name '.format(browser))


if __name__ == '__main__':
    OpenDriver().get_deriver('谷歌')
