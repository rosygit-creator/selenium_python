import pytest
from selenium.webdriver.common.by import By


class LinksPage:
    def __init__(self, driver):
        self.driver=driver

    all_links="//div[@class='jumbotron-fluid']/li/a"

    def get_url(self, url):
        self.driver.get(url)


    def get_links(self):
        links=self.driver.find_elements(By.XPATH, self.all_links)
        l1=[]
        for link in links:
            l1.append(link.get_attribute("href"))
            # print(l1)
            links_count=len(l1)
        return links_count
            # print(f"links count {len(l1)}")




