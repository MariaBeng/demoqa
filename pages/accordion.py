from pages.base_page import BasePage
from components.components import WebElement
class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver,self.base_url)

        self.elem = WebElement(driver, '#section1Content > p')
        self.elem1 = WebElement(driver, '#section1Heading')
        self.elem2 = WebElement(driver, '#section2Content > p:nth-Child(1)')
        self.elem3 = WebElement(driver, '#section2Content > p:nth-Child(2)')
        self.elem4 = WebElement(driver, '#section3Content > p')