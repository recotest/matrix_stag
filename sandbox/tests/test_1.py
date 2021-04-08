import time

from sandbox.page_objects import LoginPage


def test_one(app):
    LoginPage(app).get_login_page() \
        .set_username('') \
        .set_password('') \
        .click_login()
    time.sleep(2)
