import random
import string
import time


class Contacts:

    def __init__(self, app):
        self.app = app

    def remove_all_contacts(self):
        wd = self.app.wd

        check_all = wd.find_element_by_id("checkAll")
        check_all.click()

        bulk_actions_btn = wd.find_element_by_css_selector("[class='fal fa-tasks']")
        bulk_actions_btn.click()

        delete = wd.find_element_by_css_selector("[onclick*='Delete']")
        delete.click()

        alert_obj = wd.switch_to.alert
        alert_obj.accept()

        time.sleep(4)

    def create_contact_required(self):
        wd = self.app.wd

        add_btn = wd.find_element_by_css_selector("[href*='AddEdit']")
        add_btn.click()

        first_name = wd.find_element_by_id("FirstName")
        first_name.send_keys(''.join(random.choice(string.ascii_letters) for i in range(5)))

        last_name = wd.find_element_by_id("LastName")
        last_name.send_keys(''.join(random.choice(string.ascii_letters) for i in range(5)))

        email = wd.find_element_by_id("EmailAddress")
        email.send_keys(''.join(random.choice(string.ascii_letters) for i in range(8)) + "@gmail.com")

        save = wd.find_element_by_xpath("//*[@class='col-sm-6 mt-3']//button[@type='submit']")
        save.click()


