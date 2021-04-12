from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import TakeScreenshotConditionType, SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(
                              project_name="Workshop Python",
                              job_name="Air BNB Test")
    step_settings = StepSettings(timeout=15000,
                                 screenshot_condition=TakeScreenshotConditionType.Always,
                                 sleep_time=2000,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://www.airbnb.com"
    reporter = driver.report()

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'query'
    query = driver.find_element(By.CSS_SELECTOR,
                                "#bigsearch-query-detached-query")
    query.click()

    # 3. Type 'Hawaii' in 'query'
    query = driver.find_element(By.CSS_SELECTOR,
                                "#bigsearch-query-detached-query")
    query.send_keys("Hawaii")

    # 4. Click 'Add dates'
    add_dates = driver.find_element(By.XPATH,
                                    "//div[1]/div/div/div[. = 'Add dates']")
    add_dates.click()

    # 5. Click '21'
    _21 = driver.find_element(By.XPATH,
                              "//td[4]/div/div/div[. = '21']")
    _21.click()

    # 6. Click '23'
    _23 = driver.find_element(By.XPATH,
                              "//td[6]/div/div/div[. = '23']")
    _23.click()

    # 7. Click 'Add guests'
    add_guests = driver.find_element(By.XPATH,
                                     "//div[. = 'Add guests']")
    add_guests.click()

    # 8. Click 'SPAN'
    span = driver.find_element(By.XPATH,
                               "//div[1]/div[2]/button[2]/span")
    span.click()

    # 9. Click 'SPAN1'
    span1 = driver.find_element(By.XPATH,
                                "//div[1]/div[2]/button[2]/span")
    span1.click()

    # 10. Click 'SPAN2'
    span2 = driver.find_element(By.XPATH,
                                "//button/span/span")
    span2.click()

    # 11. Get text from 'Stays in Hawaii'
    stays_in_hawaii = driver.find_element(By.XPATH,
                                          "//h1[. = 'Stays in Hawaii']")
    step_output = stays_in_hawaii.text
    assert "Hawaii" in step_output
