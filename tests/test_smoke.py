"""
basic test
"""

import pytest


from selenium.webdriver.common.by import By


url = "https://testqastudio.me/"

def test_product_view_sku(browser):
    """
    WERT-1: Открытие деталей товара. Проверка артикула
    """
    browser.get(url=url)
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()
    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="post-11341"]')
    element.click()
    sku = browser.find_element(by=By.CSS_SELECTOR, value='[class="sku"]')

    assert sku.text == 'C0MSSDSUM7', 'Unexpected SKU for "ДИВВИНА Журнальный столик"'
 