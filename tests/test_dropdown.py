
import pytest
from pages.DropdownPage import DropdownPage
from utils.utils import *

# Navigate to a website
@pytest.mark.usefixtures("setup_driver")

class TestDropdown:
    url="https://formy-project.herokuapp.com/dropdown"

    def test_url(self):
        get_url(self.driver, self.url)
        assert "Formy" in self.driver.title

    def test_dropdown_checkbox_item(self):
        get_url(self.driver, self.url)

        dropdown_obj=DropdownPage(self.driver)
        dropdown_obj.click_dropdown()
        items=dropdown_obj.get_all_items()

        if "Checkbox" in items:
            assert "Checkbox" in items


