from selenium import webdriver
import sys
from print_styles import color

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import json



from time import sleep

class FormFillOperations:
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:4200/home")
        self.actions = ActionChains(self.driver)

    def find_element(self, xpath):
        element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
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

    def additional_cover_months_fill(self):
        extra_cover_els = self.driver.find_elements(By.NAME, 'additionalCoverMonthsInd')
        if self.additional_cover_months == 'standard':
            extra_cover_els[1].click()
        else:
            extra_cover_els[2].click()
            self.additional_cover_months = self.additional_cover_months.split()
            month_checkboxes = self.driver.find_elements(By.TAG_NAME, 'mat-checkbox')
            months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            for month in self.additional_cover_months:
                month_checkboxes[months.index(month)].click()

    def select_claim_type_from_dropdown(self, claim_type, elements, i):
        if i == 0:
            for i1, element in enumerate(elements):
                if claim_type == element.text:
                    self.down_arrow_key(i1 + 1)
                    self.enter_key()
                    break
    
    def fill_claim(self):
        self.click_element(f'//*[@id="claimsRequiredYes-button"]')

        claim_types = ['property', 'liability', 'professional indeminity']
        for i, claim in enumerate(self.claim_list_test):
            try:
                self.click_element(f'//*[@id="{claim["type"]}Ind-button"]')

                if claim['type'] != 'professionalIndemnity':
                    self.input_text(f'//*[@ng-reflect-name="claimDateMonth{str(0)}"]', claim['month'])
                    self.input_text(f'//*[@ng-reflect-name="claimDateYear{str(0)}"]', claim['year'])
                    dropdown_bar = self.driver.find_element(By.XPATH, f'//*[@ng-reflect-name="claimType{str(0)}"]')
                    dropdown_bar.click()
                    dropdown_list = dropdown_bar.find_elements(By.XPATH, './child::*')   
                    self.select_claim_type_from_dropdown(claim['main_cause'], dropdown_list, i)
                    self.input_text(f'//*[@ng-reflect-name="claimAmount{str(0)}"]', claim['amount_of_loss'])
                    self.input_text(f'//*[@ng-reflect-name="claimPostcode{str(0)}"]', claim['postcode'])
                    
                else:
                    self.input_text(f'//*[@ng-reflect-name="claimDateMonth{str(0)}"]', claim['month'])
                    self.input_text(f'//*[@ng-reflect-name="claimDateYear{str(0)}"]', claim['year'])
                    self.input_text(f'//*[@ng-reflect-name="claimDescription{str(0)}"]', claim['details'])
                    self.input_text(f'//*[@ng-reflect-name="claimAmount{str(0)}"]', claim['amount_of_loss'])
                print(color(f'Claim type {claim_types[i]} successful', text_color='dark green'))
                
            except:
                print(color(f'Claim type {claim_types[i]} failed', text_color='red'))
                sys.exit()

        self.click_element(f'//*[@id="claimsRequiredNo-button"]')

    def test_quote_page(self, trade: str):

        with open(f'fields\quotes\{trade.lower()}.json', 'r', encoding='utf8') as f:
            json_data_str = f.read()
            json_data_dict = json.loads(json_data_str)
        
        table = self.find_element('//*[@id="coverTable"]/tbody')
        table_rows = table.find_elements(By.XPATH, './/tr')
        
        for row in table_rows:
            quote_info = row.find_elements(By.XPATH, './/td')
            quote_info_str = [info.text for info in quote_info]

            cover_type_row = quote_info_str[0] + ' row'
            cover_type = quote_info_str[0]
            #check that the cover type is present in the expected body
            if cover_type_row not in json_data_dict.keys():
                print(color(f'Cover type {cover_type} not found in page', text_color='red'))
            else:
                if quote_info_str == json_data_dict[cover_type_row]:
                    print(color(f'Cover type {cover_type} passed' ,text_color = 'dark green'))
                else:
                    print(color(f'Cover type {cover_type} failed' ,text_color = 'red'))
        
        #the next steps here is to try and remove and edit quotes, similarly you can use a json object
        # also there are some additional quotes below which can each be added
        # at the end test the total value of these values, potentially also test the values of each cover


# TODO
# clean the codes to use way less lines with some smarter inheritance
# in form fill operations have methods which contain inputs and use those inputs
# in fill_form_trade have an inherited class called fields which means you will no longer have to input those fields into the main class

#need to fix the try and except loop when trying to find, input, or click an element to allow for the excpetion messages.


