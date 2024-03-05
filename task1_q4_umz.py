# mohammadreza mohammadi   40113260281818

while True:    
    def far_to_cel(far):
        cel = (far - 32) / 1.8
        return cel

    def cel_to_far(cel):
        far = (cel * 1.8) + 32
        return far

    num = input('\n\nenter 1 to fahrenhei to celsius.... enter 2 to celsius to fahrenhei  or 0 to exit... : ')
    if num == '0' :
        break
    elif num == '1':
        cel = far_to_cel(float(input('enter temperature in fahrenhei:  ')))
        print(f'the temperature in celsius is {cel}')
    elif num == '2' :
        far = cel_to_far(float(input('enter temperature in celsius:  ')))
        print(f'the temperature in fahrenhei is {far}')
    else :
        print('invalid input... please enter 1 or 2')









