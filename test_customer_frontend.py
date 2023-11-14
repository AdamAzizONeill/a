from time import sleep, time
import sys
from print_styles import color

time1 = time()

# Some inital notes
print(color('Note: In the case of a failed test, this could be due to the test itself needing refactoring.', text_color = 'red'))
print(color('Note: Currently if there is a problem with the continue button it is most likely due to some field on that page having a problem', text_color = 'red'))

try:
    from testFillFrontEnd.fill_form_plumber import form_filler  
    page1_time, page2_time, page3_time, page3_time, page5_time = form_filler.test()  

except BaseException as e:
    print(color('Issue with filling plumber form', text_color='red'))
    print(str(e))
    sys.exit()

try:
    from testFillFrontEnd.fill_form_acoustic_consultant import form_filler
    page1_time, page2_time, page3_time, page3_time, page5_time = form_filler.test()

except BaseException as e:
    print(color('Issue with filling acoustic consultant form', text_color='red'))
    print(str(e))
    sys.exit()

try:
    from testFillFrontEnd.fill_form_accountant import form_filler
    page1_time, page2_time, page3_time, page3_time, page5_time = form_filler.test(6)

except Exception as e:
    print(color('Issue with filling accountant form', text_color='red'))
    print(str(e))
    sys.exit()

try:
    from testFillFrontEnd.fill_form_cafe import form_filler
    page1_time, page2_time, page3_time, page3_time, page5_time = form_filler.test(6)

except Exception as e:
    print(color('Issue with filling cafe form', text_color='red'))
    print(str(e))
    sys.exit()



time2 = time()
total_test_time = str(round(time2 - time1, 2))
test_time_print = 'Total test time: ' + total_test_time + ' s'
print('')
print(color(test_time_print, text_color='green', is_bold=True))
print(color('All Tests Passed', text_color='green', is_bold=True))
