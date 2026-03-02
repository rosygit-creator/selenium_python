
import pytest
from pages.LinksPage import LinksPage
from utils.utils import *

# Navigate to a website
@pytest.mark.usefixtures("setup_driver")

class TestLinks:
    url="https://formy-project.herokuapp.com/"

    def test_url(self):
        get_url(self.driver, self.url)
        assert "Formy" in self.driver.title

    def test_links_count(self):
        get_url(self.driver, self.url)

        links_obj=LinksPage(self.driver)
        links_count=links_obj.get_links()

        assert links_count==14


