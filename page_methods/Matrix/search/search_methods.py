from selenium.webdriver.common.by import By


class Search:

    def __init__(self, app):
        self.app = app

    def make_resi_search(self):
        wd = self.app.wd
        act_fld = wd.find_element(By.ID, "FmFm23_Ctrl18_102_Ctrl18_TB")
        act_fld.send_keys("100")

        result_btn = wd.find_element(By.ID, "m_ucResultsPageTabs_m_lbResultsTab")
        result_btn.click()

    def street_number_width(self):
        wd = self.app.wd

        street_nmb = wd.find_element(By.CSS_SELECTOR, "[id*='0_199']")
        text = street_nmb.get_attribute("style")
        width = int(text[7:9])

        assert width == 55

        # title = wd.find_element(By.ID, "m_lblSearchName")
        # title_text = title.text
        # print()
        # print(f"The width for 'St#' filed on the {title_text} form is {str(width)}")

