import time
from pages.accordian import accordian
def test_visible_accordion(browser):
    acc = accordian(browser)
    acc.visit()
    assert acc.elem.visible()
    acc.elem1.click()
    time.sleep(2)

    assert not acc.elem.visible()


def test_visible_accordian_default(browser):
    acc = accordian(browser)
    acc.visit()
    assert not acc.elem2.visible()
    assert not acc.elem3.visible()
    assert not acc.elem4.visible()
