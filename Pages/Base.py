from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
import time

# This is Parent of all Pages


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)


    def get_title(self, title):
        WebDriverWait(self.driver, 60).until(EC.title_is(title))
        return self.driver.title

    def dropdown_select(self, by_locator, menuoption):
        sel = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
        sel.select_by_value(menuoption)

    def select_by_text(self,by_locator, menuoption):
        sel = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
        sel.select_by_visible_text(menuoption)

    def select_byindex(self, by_locator, index):
        sel = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
        sel.select_by_index(index)

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        textelemnt = element.text
        return textelemnt

    def scrol_up(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.CONTROL + Keys.HOME)

    def clear_field(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def refresh(self):
        abd = self.driver.current_url
        print(abd)
        self.driver.refresh()


    def element_to_be_clickable(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def findElement(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))

    def mouse_hover(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        ab = actions.move_to_element(element)
        ab.perform()

    def move_to_element_and_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        ab = actions.move_to_element(element)
        ab.perform()
        self.element_to_be_clickable(by_locator)

    def filter_hover(self, by_locator, locator2, filtername):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        ab = actions.move_to_element(element)
        ab.perform()
        ab = actions.click(element)
        ab.perform()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator2)).send_keys(filtername)

    def clear(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.clear()


    def switch(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.driver.switch_to.frame(element)

    def switchparent(self):
        self.driver.switch_to.parent_frame()

    def tab(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ele.send_keys(Keys.TAB)

    def get_url(self):
        url = self.driver.current_url
        return url

    def element_present(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            return True
        except NoSuchElementException:
            return False

    def window_scrol(self, by_locator):
        element = self.findElement(by_locator), time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 600)")
        # self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)

        # Click the element using JavaScript


