import sys
sys.path.append('../mcomm_form')

from time import sleep, time
from selenium.webdriver.common.by import By

import fields.acoustic_consultant_fields as acf
import fields.business_type_fields as btf 
from fields.claim_field import claim_list_test
from testFillFrontEnd.business_types import BusinessType
from print_styles import color


class AcousticsConsultantAvivaCustomerFrontendFormFill(
    BusinessType
    ):
    def __init__(
        self,
        trade: str,
        own_or_rent_business_premises: str,
        cover_assumptions: str,
        content_cover: str,
        stock_cover: str,
        transit_stock: str,
        building_cover: str,
        employer_liability: str,
        electronic_equipment: str,
        alcohol_loss: str,
        PI_cover: str,
        ATM_on_business_premises: str,
        additional_cover_months: str,
        alcohol_opposition: str,
        alcohol_refusal: str,
        alcohol_transfer: str,
        previous_claims: str,
        claim_list_test: str,
        confirm_assumptions: str,
        premises_assumption: str,
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

        #proffesstinal indeminity
        replace_existing_pi: str = None,
        retroactive_date_pi: str = None,
        annual_income: str = None,
        single_contract: str = None,
        future_claims: str = None,
        PI_cover2: str = None,
        PI_assumptions: str = None,


        ):
        self.trade = trade
        self.own_or_rent_business_premises = own_or_rent_business_premises.capitalize()
        self.cover_assumptions = cover_assumptions.capitalize()
        
        self.content_cover = content_cover
        self.stock_cover = stock_cover
        self.transit_stock = transit_stock
        self.building_cover = building_cover
        self.employer_liability = employer_liability
        self.electronic_equipment = electronic_equipment
        self.alcohol_loss = alcohol_loss
        self.PI_cover = PI_cover

        self.ATM_on_business_premises = ATM_on_business_premises.capitalize()
        self.additional_cover_months = additional_cover_months
        self.alcohol_opposition = alcohol_opposition.capitalize()
        self.alcohol_refusal = alcohol_refusal.capitalize()
        self.alcohol_transfer = alcohol_transfer.capitalize()
        self.previous_claims = previous_claims.capitalize()
        self.claim_list_test = claim_list_test
        self.confirm_assumptions = confirm_assumptions.capitalize()
        self.premises_assumption = premises_assumption.capitalize()
        self.phone_number = phone_number
        self.corresponding_address = corresponding_address.capitalize()
        self.partnership_name = partnership_name

        self.replace_existing_pi = replace_existing_pi.capitalize()
        self.retroactive_date_pi = retroactive_date_pi.capitalize()
        self.annual_income = annual_income
        self.single_contract = single_contract.capitalize()
        self.future_claims = future_claims.capitalize()
        self.PI_cover2 = PI_cover2
        self.PI_assumptions = PI_assumptions.capitalize()
        
        
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
        self.click_element('//*[@ng-reflect-name="stockCoverSelection"]', exception_message='Stock cover button on page 1')
        self.input_text('//*[@id="stockCoverAmount"]', self.stock_cover, exception_message='Stock cover amount textbox on page 1')
        self.click_element('//*[@ng-reflect-name="stockInTransitSelection"]', exception_message='Transit stock cover button on page 1')
        self.click_element(f'//*[@ng-reflect-name="stockInTransitCoverAmount{self.transit_stock}"]', exception_message='Content cover amount button on page 1')
        self.click_element('//*[@ng-reflect-name="buildingCoverSelection"]', exception_message='Building cover button on page 1')
        self.input_text('//*[@id="buildingCoverAmount"]', self.building_cover, exception_message='Building cover amount textbox on page 1')
        self.click_element('//*[@ng-reflect-name="employersLiabilitySelection"]', exception_message='Employer liability cover button on page 1')
        self.click_element('//*[@ng-reflect-name="electronicEquipmentCoverSelect"]', exception_message='Electronic equipment cover button on page 1')
        self.input_text('//*[@id="electronicEquipmentCoverAmount"]', self.electronic_equipment, exception_message='Electronic equipment cover amount textbox on page 1')
        self.click_element('//*[@ng-reflect-name="lossOfAlcoholSelection"]', exception_message='Alcohol loss cover button on page 1')
        self.click_element(f'//*[@id="lossOfAlcoholCoverAmount{self.alcohol_loss}"]', exception_message='Alcohol loss equipment cover amount textbox on page 1')
        self.click_element('//*[@ng-reflect-name="piCoverSelectionCB"]', exception_message='Professional indeminity cover button on page 1')
        self.click_element(f'//*[@id="piCoverAmount{self.PI_cover}"]', exception_message='Professional indeminity amount cover button on page 1')
        
        self.click_element('//*[@id="continueButton"]', exception_message='Continue button on page 1')

    
    def fill_page2(self):
        self.click_element(f'//*[@ng-reflect-name="displayInd{self.ATM_on_business_premises}"]', exception_message='ATM on business premises button on page 2')

        self.additional_cover_months_fill()

        self.click_element(f'//*[@ng-reflect-name="alcoholLicenceOpposition{self.alcohol_opposition}"]', exception_message='Alcohol opposition button on page 2')
        self.click_element(f'//*[@ng-reflect-name="alcoholLicenceRefusal{self.alcohol_refusal}"]', exception_message='Alcohol refusal button on page 2')
        self.click_element(f'//*[@ng-reflect-name="alcoholLicenceTransfer{self.alcohol_transfer}"]', exception_message='Alcohol transfer button on page 2')

        #intention to transfer licence in the next 12 months
        self.click_element(f'//*[@id="claimsRequired{self.previous_claims}-button"]')
        if self.previous_claims != 'no':
            self.fill_claim()

        self.test_all_business_types()

        self.input_text('//*[@id="postcodeInputText"]', self.post_code, exception_message='Postcode textbox on page 2')

        self.click_element('//app-address-lookup/div[3]/button', exception_message='Address lookup button on page 2')
        self.select_address_from_dropdown(self.address)
        self.enter_key()

        self.input_text('//*[@ng-reflect-name="emailAddress"]', self.email_address, exception_message='Email address textbox on page 2')
        self.click_element('//button[contains(text(),"Continue")]', exception_message='Continue button on page 2')



    def fill_page3(self):

        if self.PI_cover:
            self.click_element(f'//*[@ng-reflect-name="replaceExisting{self.replace_existing_pi}"]')
            if self.replace_existing_pi == 'Yes':
                self.click_element(f'//*[@ng-reflect-name="retroactiveDateInd{self.retroactive_date_pi}"]')
                if self.retroactive_date_pi == 'Yes':
                    self.click_element('//*[@aria-label="Open calendar"]')
                    sleep(0.1)
                    self.enter_key()
            self.input_text('//*[@ng-reflect-name="annualIncome"]', self.annual_income)
            self.click_element(f'//*[@ng-reflect-name="singleContractInd{self.single_contract}"]')
            self.click_element(f'//*[@ng-reflect-name="futureClaimInd{self.future_claims}"]')
            self.click_element(f'//*[@ng-reflect-value="{self.PI_cover2}"]')
            self.click_element(f'//*[@ng-reflect-name="assumptionsInd{self.PI_assumptions}"]')

            self.click_element('//button[contains(text(),"Continue")]')
            print(color('Professional Indemnity successful', text_color='dark green'))

        self.click_element('//mat-datepicker-toggle/button')
        self.enter_key()
        self.click_element(f'//*[@id="peopleAssumption{self.confirm_assumptions}"]')
        self.click_element(f'//*[@ng-reflect-name="premisesAssumption{self.premises_assumption}"]')

        sleep(0.5)
        self.click_element('//*[@type="submit"]', exception_message='Continue button on page 3')
        sleep(20)

    def fill_page4(self):

        self.click_element('//button[contains(text(),"Continue")]', exception_message='Continue button on page 4')


    def fill_page5(self):
        if 'partnership' in self.business_type.lower():
            self.input_text('//*[@ng-reflect-name="contactNameModel"]', self.contact_name, exception_message='Contact name textbox on page 5')
        self.input_text('//*[@Name="phoneNumber"]', self.phone_number, exception_message='Phone number textbox on page 5')
        self.click_element(f'//*[@ng-reflect-name="subcontractorsIndNo"]', exception_message='Correspondance address button on page 5')
        self.click_element(f'//*[@id="eltoExemptIndExempt"]', exception_message='PAYE reference number button on page 5')
        self.click_element('//button[contains(text(),"Continue")]', exception_message='Continue button on page 5')


    def test(self, stop_at_page = 6, keep_open = False):
        print(color('Starting Acoustic Consultant Test', text_color='green'))
        self.setup()
        sleep(0.2)

        if stop_at_page > 1:
            start1 = time()
            self.fill_page1()
            print(color('Page 1 successful', text_color='dark green'))
            end1 = time()
            sleep(0.3)

        if stop_at_page > 2:
            start2 = time()
            self.fill_page2()
            print(color('Page 2 successful', text_color='dark green'))
            end2 = time()
            sleep(0.3)

        if stop_at_page > 3:
            start3 = time()
            self.fill_page3()
            print(color('Page 3 successful', text_color='dark green'))
            end3 = time()
            sleep(0.3)

        if stop_at_page > 4:
            start4 = time()
            self.fill_page4()
            print(color('Page 4 successful', text_color='dark green'))
            sleep(0.3)
            end4 = time()

        if stop_at_page > 5:
            start5 = time()
            self.fill_page5()
            print(color('Page 5 successful', text_color='dark green'))
            end5 = time()

        if keep_open:
            sleep(10000)
        
        self.driver.close()
        if stop_at_page > 5:
            return end1 - start1, end2 - start2, end3 - start3, end4 - start4, end5 - start5
        
    def test_form(self):
        try:
            return self.fill_up_to_page()
        except:
            self.driver.close()
        

form_filler = AcousticsConsultantAvivaCustomerFrontendFormFill(
    acf.trade,
    acf.own_or_rent_business_premises,
    acf.cover_assumptions,
    acf.content_cover,
    acf.stock_cover,
    acf.transit_stock,
    acf.building_cover,
    acf.employer_liability,
    acf.electronic_equipment,
    acf.alcohol_loss,
    acf.PI_cover,
    acf.ATM_on_business_premises,
    acf.additional_cover_months,
    acf.alcohol_opposition,
    acf.alcohol_refusal,
    acf.alcohol_transfer,
    acf.previous_claims,
    claim_list_test,
    acf.confirm_assumptions,
    acf.premises_assumption,
    acf.phone_number,
    acf.corresponding_address,
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

    #proffessional indeminity
    acf.replace_existing_pi,
    acf.retroactive_date_pi,
    acf.annual_income,
    acf.single_contract,
    acf.future_claims,
    acf.PI_cover2,
    acf.PI_assumptions,
)
