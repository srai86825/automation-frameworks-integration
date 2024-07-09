from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestsFooter:

    @staticmethod
    @pytest.mark.subid("sub-101")
    def test_social_links(browser_driver: WebDriver, record_property):
        record_property("subid", "subid-101")
        assert browser_driver.find_element(By.XPATH, "//*[@href='https://www.linkedin.com/company/testrail/']").is_displayed()
