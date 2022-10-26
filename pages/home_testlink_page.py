from selenium import webdriver
from selenium.webdriver.common.by import By

from browser import Browser

class HomeTestelinkLocator(object):
    XPATH_GIT = "//a[.='Access Git Repository (GitHub)']"

class HomeTestelink(Browser):
    def acessarTestelink(self, url):
        self.driver.get(url)

    def clicarLinkGit(self):
        elemento = self.driver.find_element(By.XPATH, HomeTestelinkLocator.XPATH_GIT)
        elemento.click()

    