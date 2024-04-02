import Fee

print('\nPlease enter the following so we can get started with making your appointment!')

name = input('\nEnter your First Name: ')
Fee.check_name(name)

phone = input(
    '\nEnter your phone number, No space: ')  # We want the customer to enter the information so it can be able to print

Fee.check_phonenumber(phone)

address = input('\nEnter your address, No Space: ')

Fee.check_address(address)

# In this section of check, it sends back to fee to see what they entered was in letters, digits, or both
# When not entered correctly it raise ERROR so that means they have to restart and input all of the information again

print('What month are you availiable for your house to be clean?')
month = (input('\nPlease enter month number: '))
print('The month you entered was', month)

print('\n What day are you avaliable for the month you entered ')
day = (input('\nPlease enter a day number: '))
print('The day you entered was', day)

print('\nPlease enter a year')
year = (input('\nEnter year number: '))
print('The year you entered was',year)  # It is similar from the section above but it only allows for it to check numbers
# I tried setting it up where it can only range from 1-12 but it had difficulties displaying
# onto the recipt because it wont be able to display because it was a integer not a string
Fee.get_month(month)

Fee.get_day(day)

Fee.get_year(year)

tc = {1: ('2 Bedroom', 59.99), 2: ('3 Bedroom', 69.99), 3: ('4 Bedroom', 89.99), 4: ('5 Bedroom', 99.99),
      5: ('6 Bedroom', 119.99),
      6: ('Laundry', 15.99), 7: ('Deep cleaning', 29.99), 8: ('Laundry and Deep Cleaning', 39.99),
      9: ('Yard Work', 29.99), 10: ('Installing Plants', 15.99)}

print('\nThis is the cleaning service that are avliable, from 6 and above are optional!')

for a, v, in tc.items():  # For this section it allowed the customer to see what is availiable to
    # what belongs to them, the prices, and the additional cleaning for then:in line 44-47 it allowed the items to be in order from the prices to range
    # which was the point of the format
    print('{}) {}: $ {}'.format(a, v[0], v[1]))
cleaning_list = []
keep_clean = 'Y'
while keep_clean == 'Y':
    cleaning_option = int(input(
        '\nWhich cleaning plan that belongs to you? '))  # This is a while loop where allowed the customer what to pick
    # additional cleaning. If they wanted additional cleaning they would type
    # Y for yes. If not then N
    if cleaning_option in tc.keys():
        cleaning_list.append((tc[cleaning_option][0], tc[cleaning_option][1]))
    else:
        print('Invalid Choice')

    keep_clean = input('\nWould you like to select for another plan: Y for Yes and N for No: ').upper()

Fee.info_date(month, day,year)  # At the end it allowed the recipt to collect all of the information and be able   to display into the recipt we made.
Fee.info_customer(name, phone, address)
Fee.total(cleaning_list)