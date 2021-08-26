import time

def test_basket_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(10)
    basket_button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    result = False
    if len(basket_button) == 1:
        result = True
    assert result, "А где же кнопочка??? Или их так много..."
