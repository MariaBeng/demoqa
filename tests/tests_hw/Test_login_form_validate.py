from pages.practice_form import PracticeForm


def test_placeholder(browser):
    practice_form = PracticeForm(browser)

    practice_form.visit()
    assert practice_form.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert practice_form.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert practice_form.user_email.get_dom_attribute('placeholder') == 'name@example.com'

    practice_form.btn_submit.click_force()
    assert practice_form.form.get_dom_attribute('class') == 'was-validated'
