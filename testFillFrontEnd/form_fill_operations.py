from selenium import webdriver
import sys
from print_styles import color

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC



from time import sleep

class FormFillOperations:
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:4200/home")
        self.actions = ActionChains(self.driver)
        

    def find_element(self, xpath):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        x = element.location['x']
        y = element.location['y']
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (x, y)
        scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
        self.driver.execute_script(scroll_by_coord)

        return element


    def input_text(self, xpath, text, exception_message: str = None):
        element_found = False
        try:
            attempts = 0
            while attempts < 5:
                try:
                    element = self.find_element(xpath)
                    element.send_keys(text)
                    break

                except:
                    sleep(0.2)
                    attempts += 1
        except:
            if exception_message:
                if element_found:
                    full_exception_message = 'Cannot input text into' + exception_message.lower()
                else:
                    full_exception_message = exception_message + 'was not found!'
                    
                print(color(full_exception_message, text_color='red'))
            sys.exit()
        return element


    def click_element(self, xpath, exception_message: str = None):
        element_found = False
        try:
            attempts = 0
            while attempts < 5:
                try:
                    element = self.find_element(xpath)
                    element_found = True
                    element.click()
                    break
                    
                except:
                    sleep(0.2)
                    attempts += 1
        except:
            if element_found:
                full_exception_message = exception_message + 'is not clickable!'
                print(color(full_exception_message, text_color='red'))
            else:
                full_exception_message = exception_message + 'was not found!'
                print(color(full_exception_message, text_color='red'))
            sys.exit()
        return element
            


    def down_arrow_key(self, iterate):
        for k in range(iterate):
            self.actions.send_keys(Keys.ARROW_DOWN).perform()
    

    def enter_key(self):
        self.actions.send_keys(Keys.ENTER).perform()


    def select_trade_from_dropdown(self, trade, dropdown_body_xpath):
        dropdown_body = self.find_element(dropdown_body_xpath)
        dropdown_options = dropdown_body.find_elements(By.XPATH, './/*//span/span')  

        for i, dropdown_option in enumerate(dropdown_options):        
            if dropdown_option.text == trade:
                self.down_arrow_key(i + 1)
                self.enter_key()
                break
    

    def select_address_from_dropdown(self, address):
        dropdown_body = self.find_element('//app-address-lookup/select')
        dropdown_body.click()
        dropdown_options = dropdown_body.find_elements(By.XPATH, './/option')

        for i, dropdown_option in enumerate(dropdown_options):
            sleep(1)
            if address in dropdown_option.text:
                self.down_arrow_key(i + 1)
                self.enter_key()
                break

    def select_claim_type_from_dropdown(self, claim_type, elements, i):
        if i == 0:
            for i1, element in enumerate(elements):
                if claim_type == element.text:
                    self.down_arrow_key(i1 + 1)
                    self.enter_key()
                    break

    #apply downarrows and an enter when selecting the right element
    # the elements paramter are ordered as the dropdown menu shows
    #each input will either be false or will contain the non bool data.
    #below will have functions relating to exception handling

    def meant_to_be_characters(min_length: int | bool, max_length: int | bool, extra_invalid_inputs: list | bool):
        inputs =  ['1']

        if min_length:
            inputs += [min_length]

        if max_length:
            inputs += [max_length]

        if extra_invalid_inputs:
            inputs += extra_invalid_inputs
        
        return inputs

    def meant_to_be_numbers(min: int | bool, max: int | bool, extra_invalid_inputs: str | bool):
        inputs = ['a']

        if min:
            inputs += [min]

        if max:
            inputs += [max]

        if extra_invalid_inputs:
            inputs += extra_invalid_inputs
        
        return inputs
    
    def input_text_multiple_times(self, xpath, text, exception_message: str = None):
        self.input_text(self, xpath, text, exception_message)

    def detect_exception_message_under_text_box(textbox_xpath):
        pass
