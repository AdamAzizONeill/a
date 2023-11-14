business_type = 'limited partnership' #business_type (either sole trader, partnership, limited company, limited partnership)

#sole trader and partnership and limited company
business_year_start: int = '1999'
trading_name: str = 'a'
number_of_employees: str = '2'
employers_liability_coverage: str = None #select one of ('AlreadyHave', 'Exempt', 'WillBuySeperately', None)
bona_fide_subcontractors: str = 'no' #either yes or no
post_code: str = 'po168ut'
#This will have to be exactly as shown in the dropdown menu after the postcode
address: str = 'Iquo Ltd'
email_address: str = 'a@a.cc'

#sole trader
title: str = 'mr' #select from (mr, mrs, miss, ms, dr)
first_name: str = 'aa'
last_name: str = 'a'
date_of_birth: str = '11111999' # DD/MM/YYYY but as a number

#partnership
partners = [
    {'first_name' : 'aa', 'last_name': 'a'},
    {'first_name' : 'bb', 'last_name': 'b'},
]

#limited company
business_name = 'qwerty'

#limited partnership
partnership_name = 'ytrewq'

#partnership and limited partnership
contact_name = 'banana'