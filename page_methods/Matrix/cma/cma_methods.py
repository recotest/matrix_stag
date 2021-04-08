import random
import string
import time


class CMA:

    def __init__(self, app):
        self.app = app

    def start_cma(self):
        wd = self.app.wd

        start_new = wd.find_element_by_link_text("Start a New CMA")
        start_new.click()

    def select_cma_contact(self):
        wd = self.app.wd
        create_contact = wd.find_element_by_id("m_ucContacts_m_lnkAdd")
        create_contact.click()

        f_name = wd.find_element_by_css_selector("[name='m_ucContacts$m_ucAddEditContact$m_cf$m_txtPIFirstName']")
        f_name.send_keys(''.join(random.choice(string.ascii_letters) for i in range(5)))

        l_name = wd.find_element_by_css_selector("[name='m_ucContacts$m_ucAddEditContact$m_cf$m_txtPILastName']")
        l_name.send_keys(''.join(random.choice(string.ascii_letters) for i in range(5)))

        email = wd.find_element_by_css_selector("[name = 'm_ucContacts$m_ucAddEditContact$m_cf$m_txtPIEmailAddress']")
        email.send_keys(''.join(random.choice(string.ascii_letters) for i in range(8)) + "@gmail.com")

        save_btn = wd.find_element_by_css_selector("[class='linkIcon icon_save']")
        save_btn.click()

    def pages_page(self):
        wd = self.app.wd
        pages_btn = wd.find_element_by_id("m_btn_1")
        pages_btn.click()

        available_pages = wd.find_elements_by_xpath("//div[@id='m_tvCMAPages']/table/tbody//a[@class='m_tvCMAPages_0']")
        for page in available_pages:
            page.click()

    def subject_page(self):
        wd = self.app.wd
        subject_btn = wd.find_element_by_id("m_btn_2")
        subject_btn.click()

        # TODO add scenario

    def cover_page(self):
        wd = self.app.wd

        cover_btn = wd.find_element_by_id("m_btn_3")
        cover_btn.click()

        address_line_1 = wd.find_element_by_id("m_tbxContactAddress1")
        address_line_1.send_keys("Address Line 1")

        address_line_2 = wd.find_element_by_id("m_tbxContactAddress2")
        address_line_2.send_keys("Address Line 2")

        city = wd.find_element_by_id("m_tbxContactCity")
        city.send_keys("test_City")

        state = wd.find_element_by_id("m_tbxContactState")
        state.send_keys("CO")

        zip_code = wd.find_element_by_id("m_tbxContactZip")
        zip_code.send_keys(random.randint(80000, 89999))

        phone = wd.find_element_by_id("m_tbxContactPhone")
        phone.send_keys("(720) 000-0000")

    def comparables_page(self):
        wd = self.app.wd
        comparables_btn = wd.find_element_by_id("m_btn_4")
        comparables_btn.click()

        add_from_listings = wd.find_element_by_css_selector("[class='linkIcon icon_search']")
        add_from_listings.click()

        results = wd.find_element_by_css_selector("[class ='linkIcon icon_default']")
        results.click()

        all_listings = wd.find_elements_by_css_selector("[id='wrapperTable'] [type='checkbox']")

        for i in range(5):
            all_listings[i].click()

        add_listings = wd.find_element_by_css_selector("[class='linkIcon icon_add']")
        add_listings.click()

    def map_page(self):
        wd = self.app.wd

    def adjustments_page(self):
        wd = self.app.wd

    def pricing_page(self):
        wd = self.app.wd

    def finish_page(self):
        wd = self.app.wd

        finish_btn = wd.find_element_by_id("m_btn_8")
        finish_btn.click()

        time.sleep(4)
