import sys
sys.path.append('../mcomm_form')

from time import sleep, time
from print_styles import color

from testFillFrontEnd.business_types import BusinessType
from testFillFrontEnd.form_fill_operations import FormFillOperations
from fields.accountant_fields import AccountantFields
from fields.claim_field import ClaimFields

class AccountantAvivaCustomerFrontendFormFill(BusinessType, FormFillOperations, AccountantFields, ClaimFields):
    def fill_page1(self):

        self.click_element('//*[@id="onetrust-accept-btn-handler"]', exception_message='Accept cookies button')
        self.input_text('//*[@id="tradeCodeText"]', self.trade, exception_message='Trade input field on page 1')
        self.select_trade_from_dropdown(self.trade, '//*[@id="mat-autocomplete-0"]') 
        self.click_element(f'//*[@id="fixedBusinessPremises{self.own_or_rent_business_premises}-button"]', exception_message='Owning or renting fixed premises button in page 1')
        self.click_element(f'//*[@id="coverAssumptions{self.cover_assumptions}-button"]', exception_message='Confirm assumptions on page 1')
        sleep(0.2)
        self.click_element('//*[@ng-reflect-name="contentsCoverSelection"]', exception_message='Content cover button on page 1')
        self.input_text('//*[@ng-reflect-name="contentsCoverAmount"]', self.content_cover, exception_message='Content cover amount textbox on page 1')
        sleep(0.2)
        self.click_element('//*[@id="publicAndProductLiabilitySelection"]', exception_message='Stock cover button on page 1')
        self.click_element('//*[@ng-reflect-name="buildingCoverSelection"]', exception_message='Building cover button on page 1')
        self.input_text('//*[@id="buildingCoverAmount"]', self.building_cover, exception_message='Building cover amount textbox on page 1')
        self.click_element('//*[@ng-reflect-name="employersLiabilitySelection"]', exception_message='Employer liability cover button on page 1')
        self.click_element('//*[@ng-reflect-name="electronicEquipmentCoverSelect"]', exception_message='Electronic equipment cover button on page 1')
        self.input_text('//*[@id="electronicEquipmentCoverAmount"]', self.electronic_equipment, exception_message='Electronic equipment cover amount textbox on page 1')
        self.click_element('//*[@id="continueButton"]', exception_message='Continue button on page 1')

    
    def fill_page2(self):
        self.click_element(f'//*[@ng-reflect-name="displayInd{self.ATM_on_business_premises}"]', exception_message='ATM on business premises button on page 2')
        self.fill_claim(self.claim_list_test)
        self.test_all_business_types()
        
        self.input_text('//*[@id="postcodeInputText"]', self.post_code, exception_message='Postcode textbox on page 2')
        self.click_element('//app-address-lookup/div[3]/button', exception_message='Address lookup button on page 2')
        self.select_address_from_dropdown(self.address)
        self.enter_key()
        self.input_text('//*[@ng-reflect-name="emailAddress"]', self.email_address, exception_message='Email address textbox on page 2')
        self.click_element('//button[contains(text(),"Continue")]', exception_message='Continue button on page 2')


    def fill_page3(self):
        self.click_element('//mat-datepicker-toggle/button', exception_message='Date picker button on page 3')
        self.enter_key()
        self.click_element(f'//*[@id="peopleAssumption{self.confirm_assumptions}"]', exception_message='People assumption button on page 3')
        self.click_element(f'//*[@ng-reflect-name="premisesAssumption{self.premises_assumption}"]', exception_message='Premises assumption button on page 3')
        sleep(0.5)
        self.click_element('//*[@type="submit"]', exception_message='Continue button on page 3')
        sleep(20)


    def fill_page4(self):
        sleep(10000)
        self.test_quote_page(self.trade)
        self.click_element('//button[contains(text(),"Continue")]', exception_message='Continue button on page 4')

    def fill_page5(self):
        if 'partnership' in self.business_type.lower():
            self.input_text('//*[@ng-reflect-name="contactNameModel"]', self.contact_name, exception_message='Contact name textbox on page 5')
        self.input_text('//*[@Name="phoneNumber"]', self.phone_number, exception_message='Phone number textbox on page 5')
        self.click_element(f'//*[@ng-reflect-name="subcontractorsIndNo"]', exception_message='Correspondance address button on page 5')
        self.click_element(f'//*[@id="eltoExemptIndExempt"]', exception_message='PAYE reference number button on page 5')
        self.click_element('//button[contains(text(),"Continue")]', exception_message='Continue button on page 5')

    def test_pages(self):
        start_times = []
        end_times = []
        methods = (self.fill_page1, self.fill_page2, self.fill_page3, self.fill_page4, self.fill_page5)

        print(color('Starting Accountant Test', text_color='green', is_bold=True))
        self.setup()
        sleep(0.2)

        for page_number in range(1, 5 + 1):
            start_times.append(time())
            methods[page_number - 1]()
            print(color(f'Page {page_number} successful', text_color='dark green'))
            end_times.append(time())
            sleep(0.3)
        
        time_taken = [start_times_i - end_times_i for start_times_i, end_times_i in zip(start_times, end_times)]
        self.driver.close()
        return tuple(time_taken)

form_filler = AccountantAvivaCustomerFrontendFormFill()