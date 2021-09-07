# Создание фикстуры. Здесь у нас будет выполняться инициализация, как в методах SetUp и TearDown
# Также вынесем сюда все вспомогательные методы, типа autorisation, чтобы в основном файле остались только сами тесты
# И пропишем здесь импорты вебдрайвера. Чтобы браузер запускался тут
from selenium import webdriver
driver = webdriver.Firefox()

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def logout(self):
        driver = self.driver
        driver.find_element_by_xpath("//img[@alt='User avatar']").click()
        driver.find_element_by_xpath("//li[8]/button").click()
        driver.find_element_by_xpath("//footer[1]/button[1]").click()

    def autorisation(self, group):
        driver = self.driver
        driver.get("https://stepik.org/catalog?auth=login")
        driver.find_element_by_id("id_login_email").clear()
        driver.find_element_by_id("id_login_email").send_keys(group.username)
        driver.find_element_by_id("id_login_password").click()
        driver.find_element_by_id("id_login_password").clear()
        driver.find_element_by_id("id_login_password").send_keys(group.password)
        driver.find_element_by_xpath("//form[@id='login_form']/button").click()

    def open_autorisation(self):
        driver = self.driver
        driver.find_element_by_link_text('Войти').click()

    def open_catalog_page(self):
        driver = self.driver
        driver.get("https://stepik.org/catalog")

    def destroy(self):
        self.driver.quit()