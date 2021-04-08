import random
import string
import time
from datetime import date, timedelta

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime


class Input_RESI_SFR:

    def __init__(self, app):
        self.app = app
        self.id_of_listing = None
        self.price = None
        self.today = None
        self.list_agent = None
        self.login = None
        self.wait = WebDriverWait(self.app.wd, 10)

    def start_listing_tab(self):
        wd = self.app.wd

        property_subtype = Select(wd.find_element(By.ID, "Input_171"))
        property_subtype.select_by_visible_text('Single Family Residence')

        structure_type = wd.find_element(By.CSS_SELECTOR, "option[value='HOUZ']")
        structure_type.click()

        association = Select(wd.find_element(By.ID, "Input_177"))
        association.select_by_index(2)

        restrictions = Select(wd.find_element(By.ID, "Input_178"))
        restrictions.select_by_index(2)

        tax_legal_description = wd.find_element(By.ID, "Input_174")
        tax_legal_description.send_keys("Tax Legal Description tests text")

    def status_tab(self):
        wd = self.app.wd

        # status_btn = wd.find_element(By.ID, "m_rpPageList_ctl02_lbPageLink")
        status_btn = wd.find_element(By.XPATH, "//a[normalize-space()='Status']")
        status_btn.click()

        status_fld = Select(wd.find_element(By.ID, "Input_182"))
        status_fld.select_by_visible_text("Active")

    def listing_tab(self):
        wd = self.app.wd

        listing_btn = wd.find_element(By.XPATH, "//a[normalize-space()='Listing']")
        listing_btn.click()

        self.list_agent = self.login
        agent_id = wd.find_element(By.ID, "Input_146_displayValue")
        agent_id.send_keys(self.list_agent)

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='TBXFilter']")))
        wd.find_element(By.CSS_SELECTOR, "div[class='TBXFilter']").click()

        confirm_btn = wd.find_element(By.CSS_SELECTOR, "a[href*=Input_146_Refresh]")
        confirm_btn.click()

        expiration_date = wd.find_element(By.ID, "Input_181")
        self.today = date.today()
        expiration_date_value = self.today + +timedelta(random.randint(1, 14))
        expiration_date.send_keys(expiration_date_value.strftime("%m/%d/%y"))

        price_type = Select(wd.find_element(By.ID, "Input_184"))
        price_type.select_by_index(2)

        price_element = wd.find_element_by_id("Input_185")
        price_verification_element = wd.find_element_by_id("Input_1241")
        self.price = random.randint(150000, 5000000)
        price_element.send_keys(self.price)
        price_verification_element.send_keys(self.price)

        ownership = Select(wd.find_element(By.ID, "Input_186"))
        ownership.select_by_index(7)

        wd.execute_script("window.scrollTo(0, 400)")

        listing_terms_list = wd.find_elements_by_css_selector("[name='Input_188']")
        listing_terms_list[random.randrange(len(listing_terms_list))].click()

        special_listing_conditions = wd.find_elements_by_css_selector("[name='Input_189']")
        special_listing_conditions[random.randrange(len(special_listing_conditions))].click()

        wd.execute_script("window.scrollTo(0, 300)")

        buyer_agency_compensation = wd.find_element_by_id("Input_206")
        buyer_agency_compensation.send_keys(random.randint(1, 100))
        buyer_agency_compensation_type = Select(wd.find_element(By.ID, "Input_207"))
        buyer_agency_compensation_type.select_by_index(2)

        transaction_broker_compensation = wd.find_element_by_id("Input_1189")
        transaction_broker_compensation.send_keys(random.randint(1, 100))
        transaction_broker_compensation_type = Select(wd.find_element(By.ID, "Input_1190"))
        transaction_broker_compensation_type.select_by_index(2)

        dual_variable_compensation = Select(wd.find_element(By.ID, "Input_208"))
        dual_variable_compensation.select_by_index(2)

        submitted_prospect = Select(wd.find_element(By.ID, "Input_209"))
        submitted_prospect.select_by_index(2)

    def marketing_tab(self):
        wd = self.app.wd
        marketing_btn = wd.find_element(By.XPATH, "//a[normalize-space()='Marketing']")
        marketing_btn.click()

        internet_entire_listing_display = Select(wd.find_element(By.ID, "Input_198"))
        internet_entire_listing_display.select_by_index(2)

        wd.execute_script("window.scrollTo(0, 200)")

        confirm_syndication_choices = wd.find_element_by_id("Input_202")
        confirm_syndication_choices.click()

    def location_tab(self):
        wd = self.app.wd
        location_btn = wd.find_element(By.XPATH, "//a[normalize-space()='Location']")
        location_btn.click()
        # County
        all_counties = wd.find_elements_by_xpath("//select[@id='Input_221']//option")
        number_of_county = random.randint(1, len(all_counties) - 1)
        county = Select(wd.find_element(By.ID, "Input_221"))
        county.select_by_index(number_of_county)
        # Street
        street = wd.find_element_by_id("Input_222")
        street.send_keys(random.randint(1, 99999))
        # Street name
        street_name = wd.find_element_by_id("Input_224")
        street_name_val = ''.join(random.choice(string.ascii_letters + " " * 15) for f in range(20))
        street_name.send_keys(street_name_val)
        # City
        city = wd.find_element_by_id("Input_227_TB")
        city.send_keys("Denver")
        wd.find_element_by_id("Input_227_TB").send_keys(Keys.ENTER)
        # ZIP Code
        zip_code = wd.find_element_by_id("Input_228")
        zip_code.send_keys(random.randint(80000, 89999))
        # Parcel Number
        parcel_number = wd.find_element_by_id("Input_173")
        parcel_number.send_keys(random.randint(100000, 999999))
        # Tax Annual Amount
        tax_annual_amount = wd.find_element_by_id("Input_231")
        tax_annual_amount.send_keys(random.randint(500, 6500))
        # Tax Year
        tax_year = wd.find_element_by_id("Input_232")
        tax_year.send_keys(random.randint(2000, 2020))
        # Subdivision Name
        subdivision_name = wd.find_element_by_id("Input_250")
        subdivision_name.send_keys(
            str(random.randint(2000, 2020)) + " " + ''.join(
                random.choice(string.ascii_letters + " " * 15) for i in range(20)))
        # Latitude
        latitude = wd.find_element_by_id("INPUT__146")
        latitude.send_keys(str(random.uniform(36.993045, 45.001320))[0:9])
        # Longitude
        longitude = wd.find_element_by_id("INPUT__168")
        longitude.send_keys(str(random.uniform(-111.055198, -102.042131))[0:11])
        # School District
        school_district = wd.find_element_by_id('Input_397_TB')
        school_district.send_keys("Akron")
        school_district.send_keys(Keys.ENTER)
        # Elementary School
        el_school = wd.find_element_by_id('Input_252_TB')
        el_school.send_keys("Akron")
        el_school.send_keys(Keys.ENTER)
        # Middle Or Junior School
        mid_school = wd.find_element_by_id('Input_253_TB')
        mid_school.send_keys("Akron")
        mid_school.send_keys(Keys.ENTER)
        # High School
        high_school = wd.find_element_by_id('Input_254_TB')
        high_school.send_keys("Akron")
        high_school.send_keys(Keys.ENTER)

    def building_tab(self):
        wd = self.app.wd

        # TODO Different names of the tab...
        building_btn = wd.find_element_by_id('m_rpPageList_ctl08_lbPageLink')
        building_btn.click()

        year_built = wd.find_element_by_id("Input_258")
        year_built.send_keys(random.randint(1950, 2020))

        levels = wd.find_element_by_css_selector("[value='ONE']")
        levels.click()

        cons_materials = wd.find_element_by_id("Input_260_ADOB")
        cons_materials.click()

        wd.execute_script("window.scrollTo(0, 300)")

        roof = wd.find_elements_by_css_selector("[name='Input_266']")
        roof[random.randint(1, 8)].click()

        lot_size_area = wd.find_element_by_id("Input_1218")
        lot_size_area.send_keys(str(random.uniform(0.01, 9.99))[0:4])

        lot_size_measurement = Select(wd.find_element(By.ID, "Input_1219"))
        lot_size_measurement.select_by_index(1)

        # Scroll down
        wd.execute_script("window.scrollTo(0, 1000)")

        water_included = Select(wd.find_element_by_id("Input_398"))
        water_included.select_by_index(2)

    def parking_tab(self):
        wd = self.app.wd
        parking_btn = wd.find_element_by_id("m_rpPageList_ctl12_lbPageLink")
        parking_btn.click()

        paring_type = Select(wd.find_element_by_id("_Input_323__REPEAT0_302"))
        paring_type.select_by_index(2)

        of_spaces = wd.find_element_by_id("_Input_323__REPEAT0_303")
        of_spaces.send_keys(random.randint(1, 10))

    def interior_tab(self):
        wd = self.app.wd
        interior_btn = wd.find_element_by_id("m_rpPageList_ctl14_lbPageLink")
        interior_btn.click()

        above_grade = wd.find_element_by_id("Input_332")
        above_grade.send_keys(random.randint(500, 2500))

        living_area = wd.find_element_by_id("Input_334")
        living_area.send_keys(random.randint(2500, 3500))

        area_total = wd.find_element_by_id("Input_333")
        area_total.send_keys(random.randint(4500, 6000))

        basement = Select(wd.find_element_by_id("Input_176"))
        basement.select_by_index(2)

        wd.execute_script("window.scrollTo(0, 300)")

        room_type = Select(wd.find_element_by_id("_Input_1115__REPEAT0_336"))
        room_type.select_by_index(2)

        room_level = Select(wd.find_element_by_id("_Input_1115__REPEAT0_337"))
        room_level.select_by_index(2)

        # Scroll down
        # wd.execute_script("window.scrollTo(0, 300)")
        # time.sleep(1)
        # heating = wd.find_element_by_id("Input_347_ASLR")
        # heating.click()

        try:
            wd.execute_script("window.scrollTo(0, 300)")
            time.sleep(1)
            heating = wd.find_element_by_id("Input_347_ASLR")
            heating.click()
        except Exception as e:
            print(e)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            wd.get_screenshot_as_file('screenshot-%s.png' % now)

        cooling = wd.find_element_by_id("Input_348_ACRM")
        cooling.click()

    def remarks_tab(self):
        wd = self.app.wd
        remarks_btn = wd.find_element_by_id("m_rpPageList_ctl16_lbPageLink")
        remarks_btn.click()

        exclusions = wd.find_element_by_id("Input_390")
        exclusions.send_keys(''.join(random.choice(string.ascii_letters) for i in range(20)))

        contract_earnest = wd.find_element_by_id("Input_393")
        contract_earnest.send_keys(''.join(random.choice(string.ascii_letters) for i in range(20)))

    def submit_listing(self):
        wd = self.app.wd
        submit = wd.find_element_by_link_text("Submit Property")
        submit.click()
        listing_id = wd.find_element_by_id("m_lbLinkToFull")
        self.id_of_listing = listing_id.text
        print()
        print("LISTING ID: " + str(self.id_of_listing))

    def change_status_to_pending(self):
        wd = self.app.wd

        wd.get("http://reco.matrixstaging.com/Matrix/Input")
        wd.find_element(By.ID, "m_lvInputUISections_ctrl0_tbQuickEditCommonID_m_txbInternalTextBox").send_keys(
            self.id_of_listing)
        wd.find_element(By.ID, "m_lvInputUISections_ctrl0_lbQuickEdit").click()
        wd.find_element_by_link_text("Change to Pending").click()

        Select(wd.find_element(By.ID, "Input_704")).select_by_index(random.randint(1, 9))
        wd.find_element(By.ID, "Input_94").send_keys(str(date.today().strftime("%m/%d/%y")))
        wd.find_element(By.ID, "m_lbSubmit").click()

    def change_status_to_withdrawn(self):
        wd = self.app.wd

        wd.get("http://reco.matrixstaging.com/Matrix/Input")
        wd.find_element(By.ID, "m_lvInputUISections_ctrl0_tbQuickEditCommonID_m_txbInternalTextBox").send_keys(
            self.id_of_listing)
        wd.find_element(By.ID, "m_lvInputUISections_ctrl0_lbQuickEdit").click()
        wd.find_element(By.LINK_TEXT, "Change to Withdrawn").click()
        wd.find_element(By.ID, "m_lbSubmit").click()

    def change_status_to_expired(self):
        wd = self.app.wd

        wd.get("http://reco.matrixstaging.com/Matrix/Input")
        wd.find_element(By.ID, "m_lvInputUISections_ctrl0_tbQuickEditCommonID_m_txbInternalTextBox").send_keys(
            self.id_of_listing)
        wd.find_element(By.ID, "m_lvInputUISections_ctrl0_lbQuickEdit").click()

        wd.find_element(By.LINK_TEXT, "Change to Expired").click()
        wd.find_element(By.ID, "m_lbSubmit").click()

    def change_status_to_closed(self):
        wd = self.app.wd

        wd.get("http://reco.matrixstaging.com/Matrix/Input")
        wd.find_element(By.ID, "m_lvInputUISections_ctrl0_tbQuickEditCommonID_m_txbInternalTextBox").send_keys(
            self.id_of_listing)
        wd.find_element(By.ID, "m_lvInputUISections_ctrl0_lbQuickEdit").click()

        wd.find_element(By.LINK_TEXT, "Change to Closed").click()

        close_price = wd.find_element_by_id('Input_84')
        close_price_verification = wd.find_element_by_id('Input_1254')

        close_price.send_keys(self.price)
        close_price_verification.send_keys(self.price)

        commission_modified = Select(wd.find_element_by_id("Input_714"))
        commission_modified.select_by_index(3)

        buyer_financing = wd.find_elements_by_css_selector("[name='Input_715']")
        buyer_financing[random.randrange(len(buyer_financing))].click()

        close_date_el = wd.find_element_by_id("Input_85")
        close_date_el.send_keys(self.today.strftime("%m/%d/%y"))

        buyer_mls_id = wd.find_element_by_id('Input_141_displayValue')
        buyer_mls_id.send_keys(self.list_agent)
        time.sleep(2)
        buyer_mls_id.send_keys(Keys.ENTER)

        concessions = Select(wd.find_element_by_id("Input_717"))
        concessions.select_by_index(3)

        concessions_amount = wd.find_element_by_id('Input_718')
        concessions_amount.send_keys(random.randint(100, 5000))

        closing_comments = wd.find_element_by_id('Input_719')
        closing_comments.send_keys("test_test")

        wd.find_element(By.ID, "m_lbSubmit").click()

    def create_active(self):
        self.start_listing_tab()
        self.status_tab()
        self.listing_tab()
        self.marketing_tab()
        self.location_tab()
        self.building_tab()
        self.parking_tab()
        self.interior_tab()
        self.remarks_tab()
        self.submit_listing()

    def create_pending(self):
        self.create_active()
        self.change_status_to_pending()

    def create_withdrawn(self):
        self.create_active()
        self.change_status_to_withdrawn()

    def create_closed(self):
        self.create_active()
        self.change_status_to_pending()
        self.change_status_to_closed()

    def create_expired(self):
        self.create_active()
        self.change_status_to_expired()

    def populate_input_form(self, mls_status, login):

        self.login = login

        if mls_status == 'active':
            self.create_active()
        elif mls_status == 'pending':
            self.create_pending()
        elif mls_status == 'withdrawn':
            self.create_withdrawn()
        elif mls_status == 'expired':
            self.create_expired()
        elif mls_status == 'closed':
            self.create_closed()
        else:
            print("Not ready")
