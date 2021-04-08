from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def to_login_page(self):
        wd = self.app.wd
        wd.get("http://reco.matrixstaging.com/Matrix/login.aspx")

    def to_input_form(self, property_type):
        wd = self.app.wd

        wd.get("http://reco.matrixstaging.com/Matrix/Input/ListingInput")

        add_new_btn = wd.find_element(By.ID,
                                      "m_lvInputUISections_ctrl0_lvInputUISubsections_ctrl0_lbAddNewItem")
        add_new_btn.click()

        chosen_property_type = wd.find_element(By.LINK_TEXT, property_type)
        chosen_property_type.click()

        start_with_a_blank_listing = wd.find_element(By.ID, "m_rpFillFromList_ctl03_m_lbPageLink")
        start_with_a_blank_listing.click()

    def to_cma(self):
        wd = self.app.wd

        action = ActionChains(wd)
        my_matrix_element = wd.find_element_by_css_selector("[href='/Matrix/MyMatrix']")
        action.move_to_element(my_matrix_element).perform()

        cmas = wd.find_element_by_css_selector("[href*='MyMatrix/CMAs']")
        action.move_to_element(cmas).perform()
        cmas.click()

    def to_contacts(self):
        wd = self.app.wd

        action = ActionChains(wd)
        my_matrix_element = wd.find_element_by_css_selector("[href='/Matrix/MyMatrix']")
        action.move_to_element(my_matrix_element).perform()

        contacts = wd.find_element_by_css_selector("[href*='/matrix/Contacts']")
        action.move_to_element(contacts).perform()
        contacts.click()

    def to_searchForm(self, propertyType):
        wd = self.app.wd
        url = "http://reco.matrixstaging.com/Matrix/Search/" + str(propertyType)
        wd.get(url)
