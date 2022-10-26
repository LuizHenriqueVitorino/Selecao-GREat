from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from browser import Browser

class GitHubPageLocator(object):
    XPATH_AUTOR = '//a[@rel=\'author\']'
    XPATH_PESQUISA = '//form/label/input[1]'
    XPATH_CREDITO = '//div/a[@title=\'GitHub\']/../span'
    XPATH_ALL_GITHUB = '//a[.=\'search all of GitHub\']'
    XPATH_USERS = '//nav[1]/a/span[@*=\'Users\']/..'
    XPATH_URL_USER = '//a[.=\'Luiz Henrique da Silva Vitorino\']'

class GitHubPage(Browser):
    def pesquisar(self, pesquisa):
        elemento = self.driver.find_element(By.XPATH, GitHubPageLocator.XPATH_PESQUISA)
        elemento.send_keys(pesquisa)
        elemento.send_keys(Keys.ENTER)

    def clicarSearAll(self):
        elemento = self.driver.find_element(By.XPATH, GitHubPageLocator.XPATH_ALL_GITHUB)
        elemento.click()

    def clicarUsers(self):
        elemento = self.driver.find_element(By.XPATH, GitHubPageLocator.XPATH_USERS)
        elemento.click()

    def encontrarElemento(self, xpath):
        elemento = self.driver.find_element(By.XPATH, xpath)
        return elemento