from selenium.webdriver.common.by import By

from page_methods.Matrix.input.required_rules_data import *


class RequiredRulesMethods:

    def __init__(self, app):
        self.app = app
        self.warnings_text = None

    def check_required_rules(self):
        wd = self.app.wd

        wd.execute_script("window.scrollTo(0, 200)")

        validate_btn = wd.find_element(By.ID, "m_lbValidate")
        validate_btn.click()

        wd.execute_script("window.scrollTo(0, 200)")

        warn_message_text = wd.find_element(By.XPATH, "// *[contains(text(), 'were')]")
        warn_message_text.click()

        self.warnings_text = wd.find_element(By.CSS_SELECTOR, "div[id='divModalHelpContent'] ul").text

        prop_type = wd.find_element(By.ID, "m_lblInputFormName").text
        if prop_type == "Residential":
            assert self.warnings_text == resi_awi

        elif prop_type == "Residential New Home":
            assert self.warnings_text == resi_new_home_awi

        elif prop_type == "Residential Lease":
            assert self.warnings_text == rlse_awi

        elif prop_type == "Residential Income":
            assert self.warnings_text == rinc_awi

        elif prop_type == "Land":
            assert self.warnings_text == land_awi

        elif prop_type == "Farm":
            assert self.warnings_text == farm_awi

        elif prop_type == "Manufactured in Park":
            assert self.warnings_text == mprk_awi

        elif prop_type == "Commercial Sale":
            assert self.warnings_text == coms_awi

        elif prop_type == "Commercial Lease":
            assert self.warnings_text == coml_awi

        elif prop_type == "Business Opportunity":
            assert self.warnings_text == buso_awi

        elif prop_type == "Specialty":
            assert self.warnings_text == spcl_awi

        elif prop_type == "Residential Comp":
            assert self.warnings_text == comp_awi
