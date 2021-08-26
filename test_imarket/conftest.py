import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, fr, ...")

languages = ['ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr', 'it',
             'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans']

@pytest.fixture(scope="function")
def browser(request):
    lang_option = request.config.getoption("language")
    if lang_option in languages:
        options = webdriver.ChromeOptions()
        user_language = request.config.getoption("language")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru, en, fr, ... etc")
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
