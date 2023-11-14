import sys
sys.path.append('../mcomm_form')

from time import sleep, time
from selenium.webdriver.common.by import By

import fields.plumber_fields as pf
import fields.business_type_fields as btf 
from fields.claim_field import claim_list_test
from testFillFrontEnd.business_types import BusinessType
from print_styles import color

class PlumberAvivaCustomerFrontendFormFill(
    BusinessType
    ):
    def __init__(
        self,
        trade: str,
        own_or_rent_business_premises: str,
        cover_assumptions: str,
        cover_amount: str,
        ATM_on_business_premises: str,
        previous_claims: str,
        claim_list_test: str,
        confirm_assumptions: str,
        phone_number: str,
        corresponding_address: str,
        business_type: str,
        contact_name: str,

        #sole trader and partnership
        business_year_start: str,
        trading_name: str,
        number_of_employees: str,
        employers_liability_coverage: str,
        bona_fide_subcontractors: str,
        post_code: str,
        address: str,
        email_address: str,

        #sole trader
        title: str = None,
        first_name: str = None,
        last_name: str = None,
        date_of_birth: str = None,

        #partnership
        partners: dict = None,

        #limited company
        business_name: str = None,

        #limited partnership
        partnership_name: str = None,


        ):
        self.trade = trade
        self.own_or_rent_business_premises = own_or_rent_business_premises.capitalize()
        self.cover_assumptions = cover_assumptions.capitalize()
        self.cover_amount = cover_amount
        self.ATM_on_business_premises = ATM_on_business_premises.capitalize()
        self.previous_claims = previous_claims.capitalize()
        self.claim_list_test = claim_list_test
        self.confirm_assumptions = confirm_assumptions.capitalize()
        self.phone_number = phone_number
        self.corresponding_address = corresponding_address.capitalize()
        self.partnership_name = partnership_name
        
        super().__init__(
            business_year_start,
            number_of_employees,
            employers_liability_coverage,
            bona_fide_subcontractors,
            trading_name,
            title,
            first_name,
            last_name,
            date_of_birth,
            post_code,
            address,
            email_address,
            partnership_name,
            partners,
            business_name,
        )

        self.business_type = business_type
        self.contact_name = contact_name

    def fill_claim(self):
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


    def fill_page1(self):

        self.click_element('//*[@id="onetrust-accept-btn-handler"]', exception_message='Accept cookies button')
        self.input_text('//*[@id="tradeCodeText"]', self.trade, exception_message='Trade input field on page 1')
        self.select_trade_from_dropdown(self.trade, '//*[@id="mat-autocomplete-0"]') 
        self.click_element(f'//*[@id="fixedBusinessPremises{self.own_or_rent_business_premises}-button"]', exception_message='Owning or renting fixed premises button in page 1')
        self.click_element(f'//*[@id="coverAssumptions{self.cover_assumptions}-button"]', exception_message='Confirm assumptions on page 1')
        self.click_element('//*[@id="employersLiabilitySelection"]', exception_message='Employers liability cover button on page 1')
        self.click_element('//*[@id="toolsStockEquipmentSelection"]', exception_message='Tools, stock and business equipment cover button on page 1')
        self.click_element(f'//*[@id="toolStockCoverAmount{self.cover_amount}-button"]', exception_message='Tools, stock and business equipment cover select amount button on page 1')
        self.click_element('//*[@id="continueButton"]', exception_message='Continue button on page 1')

    
    def fill_page2(self):
        #self.click_element(f'//*[@id="claimsRequired{self.previous_claims}-button"]', exception_message='Previous claims button on page 2')
        #self.fill_claim()

        self.click_element(f'//*[@ng-reflect-name="claimsRequiredNo"]')
        
        try:
            self.partnership_fill_page2()
            print(color('Partnership form successful', text_color='dark green'))
        except:
            print(color('Partnership form failed', text_color='red'))
            sys.exit()
        try:
            self.limited_company_fill_page2()
            print(color('Limited Company form successful', text_color='dark green'))
        except:
            print(color('Limited Company form failed', text_color='red'))
            sys.exit()
        try:
            self.limited_partnership_fill_page2()
            print(color('Limited Partnership form successful', text_color='dark green'))
            print(color('Limited Liability Partnership form successful', text_color='dark green'))
          
        except:
            print(color('Limited Liability Partnership form failed', text_color='red'))
            print(color('Limited Partnership form failed', text_color='red'))
            sys.exit()

        try:
            self.sole_trader_fill_page2()
            print(color('Sole trader form successful', text_color='dark green'))
        except:
            print(color('Sole trader form failed', text_color='red'))
            sys.exit()

        self.input_text('//*[@id="postcodeInputText"]', self.post_code, exception_message='Postcode textbox on page 2')

        self.click_element('//app-address-lookup/div[3]/button', exception_message='Address lookup button on page 2')
        self.select_address_from_dropdown(self.address)
        self.enter_key()

        self.input_text('//*[@ng-reflect-name="emailAddress"]', self.email_address, exception_message='Email address textbox on page 2')
        self.click_element('//button[contains(text(),"Continue")]', exception_message='Continue button on page 2')


    def fill_page3(self):
        
        self.click_element('//mat-datepicker-toggle/button', exception_message='Date picker button on page 3')
        self.enter_key()
        self.click_element(f'//*[@id="peopleAssumption{self.confirm_assumptions}"]', exception_message='Confirm assumptions button on page 3')
        sleep(500)
        self.click_element('//button[contains(text(),"Continue")]', exception_message='Continue button on page 3')

    def fill_page4(self):

        self.click_element('//button[contains(text(),"Continue")]', exception_message='Continue button on page 4')


    def fill_page5(self):
        if 'partnership' in self.business_type:
            self.input_text('//*[@ng-reflect-name="contactNameModel"]', self.contact_name, exception_message='Contact name textbox on page 5')
        self.input_text('//*[@Name="phoneNumber"]', self.phone_number, exception_message='Phone number textbox on page 5')
        self.click_element(f'//*[@ng-reflect-name="subcontractorsIndNo"]', exception_message='Contact name textbox on page 5')
        self.click_element(f'//*[@id="eltoExemptIndExempt"]', exception_message='Correspondance address button on page 5')
        self.click_element('//button[contains(text(),"Continue")]', exception_message='Continue button on page 5')


    def test(self):
        print(color('Starting Plumber Test', text_color='green', is_bold=True))
        self.setup()
        sleep(0.2)

        start1 = time()
        self.fill_page1()
        print(color('Page 1 successful', text_color='dark green'))
        end1 = time()
        sleep(0.3)

        start2 = time()
        self.fill_page2()
        print(color('Page 2 successful', text_color='dark green'))
        end2 = time()
        sleep(0.3)

        start3 = time()
        self.fill_page3()
        print(color('Page 3 successful', text_color='dark green'))
        end3 = time()
        sleep(0.3)

        start4 = time()
        self.fill_page4()
        print(color('Page 4 successful', text_color='dark green'))
        sleep(0.3)
        end4 = time()

        start5 = time()
        self.fill_page5()
        print(color('Page 5 successful', text_color='dark green'))
        end5 = time()

        
        self.driver.close()
        return end1 - start1, end2 - start2, end3 - start3, end4 - start4, end5 - start5

form_filler = PlumberAvivaCustomerFrontendFormFill(
    pf.trade,
    pf.own_or_rent_business_premises,
    pf.cover_assumptions,
    pf.cover_amount,
    pf.ATM_on_business_premises,
    pf.previous_claims,
    claim_list_test,
    pf.confirm_assumptions,
    pf.phone_number,
    pf.corresponding_address,
    btf.business_type,
    btf.contact_name,

    #sole trader and partnership
    btf.business_year_start,
    btf.trading_name,
    btf.number_of_employees,
    btf.employers_liability_coverage,
    btf.bona_fide_subcontractors,
    btf.post_code,
    btf.address,
    btf.email_address,

    #sole trader
    btf.title,
    btf.first_name,
    btf.last_name,
    btf.date_of_birth,

    #partnership
    btf.partners,

    #limited company
    btf.business_name,

    #limited partnership
    btf.partnership_name,
)