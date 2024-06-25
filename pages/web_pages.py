from components.components import WebElement
from pages.base_page import BasePage

class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url= 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.rows = WebElement(driver, 'div.rt-tbody')
        self.no_rows = WebElement(driver, 'div.rt-noData')
        self.btn_delete = WebElement(driver, 'span[title = Delete]')
        self.btn_add = WebElement(driver, 'button.btn-primary')
        self.registration_form = WebElement(driver, 'div.modal-content')
        self.btn_submit = WebElement(driver, 'form  > div > div > button.btn-primary')

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.new_row = WebElement(driver, "//*[text()='cherry']", 'xpath')
        self.new_btn_add = WebElement(driver, "//*[@id='edit-record-4']", 'xpath')
        self.edit_row = WebElement(driver, "//*[text()='cherry2']", 'xpath')
        self.btn_delete_new_row = WebElement(driver, "//*[@id='delete-record-4']", 'xpath')