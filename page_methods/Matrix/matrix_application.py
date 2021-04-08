from selenium import webdriver

from page_methods.Matrix.cma.cma_methods import CMA
from page_methods.Matrix.contacts.contacts_methods import Contacts
from page_methods.Matrix.input.input_resi_sfr_methods import Input_RESI_SFR
from page_methods.Matrix.input.required_rules_methods import RequiredRulesMethods
from page_methods.Matrix.search.search_methods import Search
from page_methods.Matrix.сommon_methods.navigationhelper import NavigationHelper
from page_methods.Matrix.сommon_methods.session import SessionHelper


class MatrixApp:

    def __init__(self):
        #  For Chrome headless mode
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--start-maximized')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # self.wd = webdriver.Chrome(options=chrome_options)

        #  For Chrome with browser
        # self.wd = webdriver.Chrome()

        #  For FireFox headless mode
        fire_fox_options = webdriver.FirefoxOptions()
        fire_fox_options.add_argument('--headless')
        fire_fox_options.add_argument('--start-maximized')
        fire_fox_options.add_argument('--disable-dev-shm-usage')
        self.wd = webdriver.Firefox(options=fire_fox_options)

        #  For FireFox with browser
        # self.wd = webdriver.Firefox()

        self.wd.set_window_size(1920, 1080)
        self.wd.implicitly_wait(3)

        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.search = Search(self)
        self.resi_sfr = Input_RESI_SFR(self)
        self.cma = CMA(self)
        self.contacts = Contacts(self)
        self.valid_rules = RequiredRulesMethods(self)

    def destroy(self):
        self.wd.close()
        self.wd.quit()
