import time
from pages.accordion import Accordion
def test_visible_accordion(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert accordion.elem.visible()
    accordion.elem1.click()
    time.sleep(2)

    assert not accordion.elem.visible()


def test_visible_accordion_default(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert not accordion.elem2.visible()
    assert not accordion.elem3.visible()
    assert not accordion.elem4.visible()
