from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url= 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_third_menu = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > span > div > div.header-right > div.icon > svg')
        self.icon = WebElement(driver, '#app > header > a > img')