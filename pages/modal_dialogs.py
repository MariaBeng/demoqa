from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url= 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_third_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a > img')
        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.small_modal_cls = WebElement(driver, '#closeSmallModal')
        self.large_modal_cls = WebElement(driver, '#closeLargeModal')