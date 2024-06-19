from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    assert modal_dialogs.btns_third_menu.check_count_elements(count=5)


def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    modal_dialogs.refresh()

    modal_dialogs.icon.click()
    modal_dialogs.back()

    browser.set_window_size(900, 400)

    modal_dialogs.forward()
    assert modal_dialogs.get_url()
    assert browser.title == "DEMOQA"

    browser.set_window_size(1000, 1000)








