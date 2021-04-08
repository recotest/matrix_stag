from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd

        login_fld = wd.find_element(By.ID, "m_tbName")
        login_fld.clear()
        login_fld.send_keys(username)

        psw_fld = wd.find_element(By.ID, "m_tbPassword")
        psw_fld.clear()
        psw_fld.send_keys(password)

        login_btn = wd.find_element(By.ID, "m_imgbtnLogin")
        login_btn.click()

        try:
            dismiss_btn = wd.find_element(By.ID, "ctl02_ctl04_HyperLink1")
            dismiss_btn.click()
        except NoSuchElementException:
            pass
        except ElementNotInteractableException:
            pass
        try:
            ive_read_this_btn = wd.find_element(By.CSS_SELECTOR, "#NewsDetailDismissNew")
            ive_read_this_btn.click()
        except NoSuchElementException:
            pass
        except ElementNotInteractableException:
            pass

    def logout(self):
        wd = self.app.wd

        wd.get("http://reco.matrixstaging.com/Matrix/MyMatrix")

        user_name_btn = wd.find_element(By.CSS_SELECTOR, "[id*='ctl02_ctl01_m_lblHeading']")
        user_name_btn.click()

        logout_btn = wd.find_element(By.CSS_SELECTOR, "[href*='Logout.aspx']")
        logout_btn.click()
