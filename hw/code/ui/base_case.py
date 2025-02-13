import pytest
from _pytest.fixtures import FixtureRequest

from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.login import LoginPage
from hw.code.ui.pages.movie_page import MoviePage
from hw.code.ui.pages.profile_page import ProfilePage
from hw.code.ui.pages.register import RegPage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)
        self.serial_page = MoviePage(driver)
        self.profile_page = ProfilePage(driver)
        self.reg_page = RegPage(driver)
        if self.authorize:
            credentials = request.getfixturevalue('credentials')
            login_page = LoginPage(driver)
            login_page.login(*credentials)
