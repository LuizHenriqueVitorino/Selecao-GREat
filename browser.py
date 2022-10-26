
from selenium import webdriver

class Browser(object):
    # Inicia o browser no FireFox
    driver = webdriver.Firefox()
    # Define o tempo máximo para carregamento da página
    driver.set_page_load_timeout(30)
    # Maximixa a janela do browser ao ser iniciada
    driver.maximize_window()

    # Fecha o browser
    def browser_quit(self):
        self.driver.quit()

    # Limpa o browser
    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
    
    def browser_wait(self, seconds):
        self.driver.implicitly_wait(seconds)