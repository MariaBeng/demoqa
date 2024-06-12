from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.get_text()
    demo_qa_page.text.click()

    assert demo_qa_page.equal_url()
    assert demo_qa_page.get_text()

def test_check_text1(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    elements_page = ElementsPage(browser)
    demo_qa_page.btn_elements.click()
    demo_qa_page.get_text1()
    demo_qa_page.text1.click()
    assert elements_page.equal_url()
    assert demo_qa_page.get_text1()

