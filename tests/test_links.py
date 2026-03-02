from selenium import webdriver
import pytest
from pages.LinksPage import LinksPage

# Navigate to a website
@pytest.mark.usefixtures("setup_driver")

class TestLinks:
    def test_links_count(self):
        links_obj=LinksPage(self.driver)
        links_obj.get_url("https://formy-project.herokuapp.com/")
        links_count=links_obj.get_links()

        assert links_count==14


