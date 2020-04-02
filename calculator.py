def welcome():
    print('''
    Welcome to Calculator
    ''')
def sum(firstOperand, secondOperand):
    sum = firstOperand + secondOperand
    print('The sum is: {0}'.format(sum))


def difference(firstOperand, secondOperand):
    difference = firstOperand - secondOperand
    print('The difference is: {0}'.format(difference))

def multiplication(firstOperand, secondOperand):
    product = firstOperand * secondOperand
    print('The product is: {0}'.format(product))

def division(firstOperand, secondOperand):
    quotient = firstOperand / secondOperand
    remainder = firstOperand % secondOperand
    print('The quotient is: {0}'.format(quotient))
    print('The remainder is: {0}'.format(remainder))


#this function asks for user if he want to do a new calculation
def again():
    choice = input('Do you want to make a new calculation? Type N for no, type Y for yes.\n')

    if choice.upper() == 'Y':
        return 1
    elif choice.upper() == "N":
        return 0
    else:
        print('Please choose a valid symbol.\n')
        again()


# this function does the calculation requested by user
def calculate():

    firstOperand = int(input('Give me the first operand:\n'))
    secondOperand = int(input('Give me the second operand:\n'))

    operation = input('What action do you want to do? \n Type: \n + for a sum \n - for a subtraction \n * or a multiplication \n / for a division\n')

    if operation == '+':
        sum(firstOperand, secondOperand)

    elif operation == '-':
       difference(firstOperand, secondOperand)

    elif operation == '*':
        multiplication(firstOperand, secondOperand)

    elif operation == '/':
        division(firstOperand, secondOperand)

    else:
        print('Please choose a valid symbol.\n')
        

def start():
    calculate()
    while again() ==  True:
        calculate()
    print('Thanks for using my calculator, see you soon!!\n')


start()

