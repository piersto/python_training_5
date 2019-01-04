import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    base_url = request.config.getoption('--baseUrl')
    secret_password = request.config.getoption('--secret_password')
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url, secret_password=secret_password)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url, secret_password=secret_password)
    fixture.session.ensure_login(username="admin", password=secret_password)
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--baseUrl', action='store', default='http://localhost/addressbook/')
    parser.addoption('--secret_password', action='store', default='secret')


