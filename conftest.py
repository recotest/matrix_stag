import pytest

from page_methods.Matrix.matrix_application import MatrixApp
from selenium.webdriver import Chrome


@pytest.fixture(scope="session")
def app(request):
    fixture = MatrixApp()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(scope="session")
def test_app():
    driver = Chrome()
    return driver
