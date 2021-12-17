from selenium.webdriver.common.by import By
from POMDemo.Locators.HomePageLocators import HomePageLocators

class Homepage():
    def __init__(self,driver):
        self.driver = driver

    def click_welcome_link(self):
        self.driver.find_element(By.ID, HomePageLocators.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, HomePageLocators.logout_link_linkText).click()