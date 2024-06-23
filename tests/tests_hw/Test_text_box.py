from pages.text_box import TextBox
import time

def test_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys('Cherry')
    text_box.current_address.send_keys('Saint P')

    text_box.btn_submit.click_force()
    time.sleep(5)
    assert text_box.checking.get_text() == 'Name:Cherry\nCurrent Address :Saint P'
