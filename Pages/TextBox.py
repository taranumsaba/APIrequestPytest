import time

from selenium.webdriver.common.by import By
from Pages.Base import BasePage
from Config.CustomLogger import LogGen


class TextBox(BasePage):
    #   ********By Locators************
    element = (By.XPATH, '//h5[text()="Elements"]/parent::div/parent::div')
    textbox = (By.XPATH, '//span[text()="Text Box"]')
    full_name_input = (By.ID, "userName")
    email_input = (By.ID, "userEmail")
    current_address_input = (By.ID, "currentAddress")
    permanent_address_input = (By.ID, "permanentAddress")
    submit_button = (By.ID, "submit")
    logger = LogGen.loggen()

    # **********Constructor of BasePage Class********
    def __init__(self, driver):
        super().__init__(driver)



    # **********   Page Actions  ***************
    # This function called to validate login credentials
    def click_element(self):
        time.sleep(2)
        url = "https://demoqa.com/elements"
        actual_url = self.get_url()
        if actual_url != url:
            self.logger.info("***********  Click Element **********************")
            self.window_scrol(self.element)
            self.do_click(self.element)

    def click_textbox(self):
        time.sleep(3)
        self.logger.info("***********  Click Textbox *********************")
        self.refresh()
        self.do_click(self.textbox)

    def enter_full_name(self, name):
        time.sleep(3)
        self.logger.info("***********  Enter Name **********************")
        self.do_send_keys(self.full_name_input, name)
        element_text = self.get_text(self.full_name_input)
        return element_text

    def enter_email(self, email):
        time.sleep(3)
        self.logger.info("***********  Enter Email **********************")
        self.do_send_keys(self.email_input, email)
        element_text = self.get_text(self.email_input)
        return element_text

    def enter_current_address(self, address):
        time.sleep(3)
        self.logger.info("***********  Enter Current Address **********************")
        self.do_send_keys(self.current_address_input, address)
        element_text = self.get_text(self.current_address_input)

        return element_text

    def enter_permanent_address(self, address):
        time.sleep(3)
        self.logger.info("***********  Enter Permanent Address **********************")
        self.do_send_keys(self.permanent_address_input, address)
        element_text = self.get_text(self.permanent_address_input)
        return element_text

    def click_submit(self):
        time.sleep(3)
        self.window_scrol(self.submit_button)
        self.do_click(self.submit_button)

        time.sleep(4)

