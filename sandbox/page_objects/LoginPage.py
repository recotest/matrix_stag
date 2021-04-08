from sandbox.locators import LoginPage as LP
from .BasePage import BasePage


class LoginPage(BasePage):

    def get_login_page(self):
        self.driver.get("http://reco.matrixstaging.com/Matrix/login.aspx")

    def set_username(self, username):
        self._input(LP.username, "zialio")
        return self

    def set_password(self, password):
        self._input(LP.password, "In2knp2ts")
        return self

    def click_login(self):
        self._click(LP.login_btn)
