# mohammadreza mohammadi   40113260281818
total = 0
def deposit():
    global total
    amount = float(input('please enter the amount you want to deposit :  '))
    total += amount
    print(f'your total amount increased... total amount: {total}')

def withdraw():
    global total
    amount = float(input('please enter the amount you want to withdraw :  '))
    if total >= amount :
        total -= amount
        print(f'your total amount decreased... total amount: {total}')
    else:
        print('total amount is not enough')

def check_total():
    print(f'total amount : {total}')
    



while True:
    print('\n\nplease choose')
    print('1.deposit')
    print('2.withdraw')
    print('3.check total')
    print('4.exit')
    num = input('enter your choose:  ')
    if num == '1':
        deposit()

    elif num == '2':
        withdraw()

    elif num == '3':
        check_total()

    elif num == '4':
        print('thanks for using this program')
        break
    else :
        print('please enter right number  \n')



