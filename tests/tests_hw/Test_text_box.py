from pages.text_box import TextBox
import time

Name = 'Cherry'
Address = 'Saint P'

def test_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys(Name)
    text_box.current_address.send_keys(Address)

    text_box.btn_submit.click_force()
    time.sleep(5)
    assert text_box.checking.get_text() == f'Name:{Name}\nCurrent Address :{Address}'
