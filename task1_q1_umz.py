# mohammadreza mohammadi   40113260281818
while True :
    num = input('if you wanna exit enter 0 else enter anything... :  ')
    if num == '0':
        break

    def analyze (n):
        if n.isdigit():
            return int(n) , 'digit'
        elif all( item.isalpha() or item.isdigit()  for item in n):
            return n , 'string'
        else : 
            return n.split() , 'list'
    n = input('please enter your input... :  ')
    result , data_type = analyze(n)
    print(f'data type :   {data_type}')
    print(f'output :   {result}')




