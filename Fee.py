# Part 1 of the project setting an appointment and getting the amount of the cleaning appointment
fout = open('recipt.txt', 'w')


class Worker:
    def __init__(self):  # Adding a worker to the program, adding ID just for extra
        self.name = None


class Maid(Worker):
    def __init__(self):
        super().__init__()
        self.ID = None


Employee1 = Maid()
Employee1.name = 'Laura A Robles'
Employee1.ID = '#1519'

fout.write('***WORKER INFORMATION***\n\nEmployee Name: ')
fout.write(Employee1.name)  # In this section I indidcated fout.write, to add information, and
fout.write('\nEmployee Number: ')  # designing th recipt. Adding the worker into the recipt
fout.write(Employee1.ID)
fout.write('\n''\n')


def get_month(month):
    if month.isdigit():
        print('The month is: ', month)  # when adding definition of the keywords, it help me
    else:
        raise Exception('You did not enter a valid phone number!')  # to add the customer information into the recipt


def get_day(day):
    if day.isdigit():
        print('The day of your appointment is going to be on: ', day)
    else:
        raise Exception('You did not enter a valid phone number!')


def get_year(year):
    if year.isdigit():
        print('the year of the appointment is on: ', year)
    else:
        raise Exception(
            'You did not enter a valid phone number!')  # With it including all of the information. Such as year date and etc


def info_date(month, day, year):
    fout.write('**** RECIPT DATE ****\n')
    fout.write('----             ----\n')
    fout.write(month + '/')
    fout.write(day + '/')
    fout.write(year)
    fout.write('\n')
    fout.write('----             ----\n')


def check_name(name):
    if name.isalpha():
        print('Your name:', name)
    else:
        raise Exception('You did not enter a valid Name!')


def check_phonenumber(phone):
    if phone.isdigit():
        print('Your phone number is: ', phone)
    else:
        raise Exception('You did not enter a valid phone number!')


def check_address(address):
    if address.isalnum():
        print('Your address is: ', address)
    else:
        raise Exception('You did not enter a valid address number!')


def info_customer(name, phone, address):
    fout.write('\n')
    fout.write('***CUSTOMER INFO***\n')
    fout.write('---             ---\n')
    fout.write(name + '\n')
    fout.write(phone + '\n')
    fout.write(address + '\n')
    fout.write('---             ---\n')


downpayfee = 20
tax = 0.01


def total(cleaning_list):
    subtotal = 0

    for i in cleaning_list:
        subtotal += (i[1])

    print(cleaning_list)
    print('Subtotal: $ {:.2f}'.format(subtotal))

    t_amount = tax * subtotal
    print('Tax: \t$ {:.2f}'.format(t_amount))

    downpayment = downpayfee
    print('Downpayment fee: \t$ {:.2f}'.format(downpayment))

    total = subtotal + t_amount + downpayment
    print('Total: \t$ {:.2f}'.format(total))

    recipt(cleaning_list, subtotal, total, downpayment)


def recipt(cleaning_list, subtotal, total, downpayment):
    fout.write('**** RECIPT ****\n')
    fout.write('Choice        Price\n')
    fout.write('----        ------\n')

    for i in cleaning_list:
        fout.write('{} $ {}\n'.format(i[0], i[1]))

    fout.write('''
--------------------------------
subtotal:   ${}
downpayment: ${:.2f}
Tax:        %{}
Total:      ${:.2f}
--------------------------------
Thank you for shopping with us...
'''.format(subtotal, downpayment, tax * 100, total))

    fout.close()
    print('\nThank you for setting your appointment hope to see you again!\nHave a great Day!')
    print('\nPlease Check your files to see the recipt!\nThank you again!')