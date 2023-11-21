claim_list_test = [
    {
        'type': 'property', #either property, liability, professionalIndemnity
        'month': '01', #mm
        'year': '2020', #yyyy              needs to be in the last five years
        'main_cause': 'Falling Trees', #select from the dropdown, put exacltly as shown
        'amount_of_loss': '100',
        'postcode': 'PO168U'
    },
    {
        'type': 'liablity', #either property, liability, professionalIndemnity
        'month': '01', #mm
        'year': '2020', #yyyy              needs to be in the last five years
        'main_cause': 'Falling Trees', #select from the dropdown, put exacltly as shown
        'amount_of_loss': '1',
        'postcode': 'T'
    },
    {
        'type': 'professionalIndemnity',
        'month': '01', #mm
        'year': '2020', #yyyy              needs to be in the last five years
        'details': 'broke a leg',
        'amount_of_loss': '2',

    },
]