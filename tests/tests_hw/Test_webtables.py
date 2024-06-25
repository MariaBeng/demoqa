import time
from pages.web_pages import WebTables

# def test_web_tables(browser):
#     web_tables = WebTables(browser)
#
#     web_tables.visit()
#     assert web_tables.rows.exist()
#     assert not web_tables.no_rows.exist()
#
#     while web_tables.btn_delete.exist():
#        web_tables.btn_delete.click()
#
#     time.sleep(3)
#     assert web_tables.no_rows.exist()

def test_add(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    web_tables.btn_add.exist()
    web_tables.btn_add.click()
    assert web_tables.registration_form.exist()
    web_tables.btn_submit.click_force()
    assert web_tables.registration_form.exist()
    time.sleep(1)

    web_tables.first_name.send_keys('cherry')
    web_tables.last_name.send_keys('Skl')
    web_tables.user_email.send_keys('Cherry@gmail.com')
    web_tables.age.send_keys('100')
    web_tables.salary.send_keys('10000000')
    web_tables.department.send_keys('test')
    time.sleep(1)
    web_tables.btn_submit.click()
    time.sleep(1)
    assert not web_tables.registration_form.exist()
    assert web_tables.new_row.exist()

    web_tables.new_btn_add.click()
    assert web_tables.registration_form.exist()

    web_tables.first_name.clear()
    web_tables.first_name.send_keys('cherry2')
    web_tables.btn_submit.click()
    assert web_tables.edit_row.exist()

    web_tables.btn_delete_new_row.click()
    assert not web_tables.edit_row.exist()

