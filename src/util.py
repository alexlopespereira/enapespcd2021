from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element(driver, by_content, by=By.XPATH, timeout=8):
    try:
        element_present = EC.presence_of_element_located((by, by_content))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
        return False
    return True


def remove_element(driver, element):
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)