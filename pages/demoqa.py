from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement
class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver,self.base_url)

        self.icon = WebElement(driver,'#app > header > a')
        self.btn_elements = WebElement(driver,"#app > div > div > div.home-body > div > div:nth-child(1)")
        self.text = WebElement(driver, "#app > footer > span")
        self.text1 = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6")
    def exist_icon(self):
        try:
            self.icon.find_element()
        except NoSuchElementException:
            return False
        return True

    # def exist_text(self):
    #     try:
    #         self.driver.text(str("© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."))
    #     except NoSuchElementException:
    #         return False
    #     return True

    def get_text(self):
        if self.text.get_text() == str("© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."):
            return True
        else:
            return False

    def get_text1(self):
        if self.text1.get_text() == str("Please select an item from left to start practice."):
            return True
        else:
            return False





    # def click_on_the_icon(self):
    #     self.find_element(locator = '#app > header > a').click()
    #
    # def click_on_the_btn(self):
    #     self.find_element(locator = "#app > div > div > div.home-body > div > div:nth-child(1)").click()


