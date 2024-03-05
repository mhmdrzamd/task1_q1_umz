# mohammadreza mohammadi   40113260281818

while True:
    operator = input('\n\nenter operator (sum , diffrence , multiple , devide)  and enter 0 if you wanna exit :  ')
    
    if operator == '0' :
        break

    num1 = float(input('enter number 1 : '))
    num2 = float(input('enter number 2 : '))

    if operator == 'sum':
        result = num1 + num2
    elif operator == 'diffrence':
        result = num1 - num2
    elif operator == 'multiple':
        result = num1 * num2
    elif operator == 'devide':
        result = num1 / num2
    else :
        print('invalid input...please enter correct input  ')
    print(f'the result is {result}')





