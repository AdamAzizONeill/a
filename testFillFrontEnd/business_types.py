from testFillFrontEnd.form_fill_operations import FormFillOperations
from time import sleep
import sys
from print_styles import color

class BusinessType(FormFillOperations):
    def __init__(
        self,
        business_year_start: str,
        number_of_employees: str,
        employers_liability_coverage: str,
        bona_fide_subcontractors: str,
        trading_name: str,
        title: str,
        first_name: str,
        last_name: str,
        date_of_birth: str,
        post_code: str,
        address: str,
        email_address: str,
        partnership_name: str,
        partners: list,
        business_name: str,
            ):
        self.business_year_start = business_year_start
        self.partnership_name = partnership_name
        self.trading_name = trading_name
        self.partners = partners
        self.number_of_employees = number_of_employees
        self.employers_liability_coverage = employers_liability_coverage
        self.bona_fide_subcontractors = bona_fide_subcontractors.capitalize()
        self.post_code = post_code
        self.address = address
        self.email_address = email_address
        self.title = title.capitalize()
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.business_name = business_name

    
    def sole_trader_fill_page2(self):
        business_type_el = self.click_element('//*[@ng-reflect-name="soleTraderInd"]', exception_message='Sole trader button on page 2')
        html_el = business_type_el.get_attribute('innerHTML')
        if 'aria-pressed="false"' in html_el:
            self.click_element('//*[@ng-reflect-name="soleTraderInd"]', exception_message='Sole trader button on page 2')
        self.input_text('//*[@ng-reflect-name="yearEstablished"]', self.business_year_start, exception_message='Year established on page 2')
        self.input_text('//*[@ng-reflect-name="tradingName"]', self.trading_name, exception_message='Trading name on page 2')
        self.input_text('//*[@ng-reflect-name="numberOfEmployees"]', self.number_of_employees, exception_message='Number of employees on page 2')
        if self.employers_liability_coverage:
            self.click_element(f'//*[@id="{self.employers_liability_coverage}-button"]', exception_message='Employers liability coverage on page 2')
        self.click_element(f'//*[@id="subcontractorsInd{self.bona_fide_subcontractors}"]', exception_message='Bona Fide Subcontractors button on page 2')
        self.click_element(f'//*[@id="titleModel{self.title}"]', exception_message='Title button on page 2')
        self.input_text('//*[@ng-reflect-name="forenameModel"]', self.first_name, exception_message='First name on page 2')
        self.input_text('//*[@ng-reflect-name="surnameModel"]', self.last_name, exception_message='Last name on page 2')
        self.input_text('//*[@id="dateOfBirthModel"]', self.date_of_birth, exception_message='Date of birth button on page 2')


    def partnership_fill_page2(self):
        business_type_el = self.click_element('//*[@ng-reflect-name="partnershipInd"]', exception_message='Partnership button on page 2')
        html_el = business_type_el.get_attribute('innerHTML')
        if 'aria-pressed="false"' in html_el:
            self.click_element('//*[@ng-reflect-name="partnershipInd"]', exception_message='Partnership button on page 2')
        self.input_text('//*[@ng-reflect-name="yearEstablished"]', self.business_year_start, exception_message='Year established on page 2')
        self.input_text('//*[@ng-reflect-name="tradingName"]', self.trading_name, exception_message='Trading name on page 2')
        sleep(0.2)
        self.input_text('//*[@ng-reflect-name="numberOfPartners"]', str(len(self.partners)))
        #sleep(0.2)
        for i, partner in enumerate(self.partners):
            self.input_text(f'//*[@ng-reflect-name="forename{i}"]', partner['first_name'], exception_message='First name on page 2')
            self.input_text(f'//*[@ng-reflect-name="surname{i}' + '}"]', partner['last_name'], exception_message='Last name on page 2')
        self.input_text('//*[@ng-reflect-name="numberOfEmployees"]', self.number_of_employees, exception_message='Number of employees on page 2')
        if self.employers_liability_coverage:
            self.click_element(f'//*[@id="{self.employers_liability_coverage}-button"]', exception_message='Employers liability coverage on page 2')
        self.click_element(f'//*[@id="subcontractorsInd{self.bona_fide_subcontractors}"]', exception_message='Bona Fide Subcontractors button on page 2')


    def limited_company_fill_page2(self):
        business_type_el = self.click_element('//*[@ng-reflect-name="limitedCompanyInd"]', exception_message='Limited button company on page 2')
        html_el = business_type_el.get_attribute('innerHTML')
        if 'aria-pressed="false"' in html_el:
            self.click_element('//*[@ng-reflect-name="limitedCompanyInd"]', exception_message='Limited company button on page 2')
        self.input_text('//*[@ng-reflect-name="yearEstablished"]', self.business_year_start, exception_message='Year established on page 2')
        self.input_text('//*[@ng-reflect-name="registeredName"]', self.business_name, exception_message='Business name button on page 2')
        self.input_text('//*[@ng-reflect-name="tradingName"]', self.trading_name, exception_message='Trading name on page 2')
        self.input_text('//*[@ng-reflect-name="numberOfPartnersAndEmployees"]', self.number_of_employees, exception_message='Number of employees on page 2')
        if self.employers_liability_coverage:
            self.click_element(f'//*[@id="{self.employers_liability_coverage}-button"]', exception_message='Employers liability coverage on page 2')
        self.click_element(f'//*[@id="subcontractorsInd{self.bona_fide_subcontractors}"]', exception_message='Bona Fide Subcontractors button on page 2')


    def limited_partnership_fill_page2(self):
        business_type_el = self.click_element('//*[@ng-reflect-name="limitedPartnershipInd"]', exception_message='Limited partnership button on page 2')
        html_el = business_type_el.get_attribute('innerHTML')
        if 'aria-pressed="false"' in html_el:
            self.click_element('//*[@ng-reflect-name="limitedPartnershipInd"]', exception_message='Limited partnership button on page 2')
        self.input_text('//*[@ng-reflect-name="registeredName"]', self.partnership_name, exception_message='Partnership on page 2')
        self.input_text('//*[@ng-reflect-name="yearEstablished"]', self.business_year_start, exception_message='Year established on page 2')
        self.input_text('//*[@ng-reflect-name="tradingName"]', self.trading_name, exception_message='Trading name on page 2')
        self.input_text('//*[@ng-reflect-name="numberOfPartners"]', str(len(self.partners)), exception_message='Number of partners on page 2')
        self.input_text('//*[@ng-reflect-name="numberOfEmployees"]', self.number_of_employees, exception_message='Number of employees on page 2')
        if self.employers_liability_coverage:
            self.click_element(f'//*[@id="{self.employers_liability_coverage}-button"]', exception_message='Liability coverage on page 2')
        self.click_element(f'//*[@id="subcontractorsInd{self.bona_fide_subcontractors}"]', exception_message='Bona Fide Subcontractors button on page 2')  


    def test_all_business_types(self):
        
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
            print(color('Sole trader form failed', text_color='dark green'))
            sys.exit() 