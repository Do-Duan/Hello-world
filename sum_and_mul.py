
def sum_and_mul():
    number1 = int(input('Number 1 :'))
    number2 = int(input('Number 2 :'))
    print('The sum is ' + str(number2 + number1))
    print(f'The multiplication {number1 * number2}')

def iterate_first_10_numbers():
    for i in range(10):
        curent = i
        previous = i -1
        if(previous < 0):
            previous = 0
        sum = curent + previous
        print(f'Current number {curent}, Previous number {previous} , Sum: {sum}')


while True:
    try:
        choice = int(input('1. sum and multiplication\n'
                           '2. iterate_first_10_numbers\n'
                           '3. Exit \n'))
        match choice:
            case 1:
                sum_and_mul()

            case 2:
                iterate_first_10_numbers()
            case 3: break
    except:
        print('Re-input')


