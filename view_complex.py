def view_data(data, title):
    print(f'{title} = {data}')

def get_value(a):
    return int(input(f'value  {a} = '))

def get_function():
    return input('input on of: +, -, *, / -->> ')



def cho():
    x = ''
    while x not in {'c','r','e'}:
        x = input('Used complex or rational or exit = c/r/e? ')
        if x not in {'c','r','e'}:
            return -1
        if x == 'c':
            return 2
        if x == 'r':
            return 1
        if x == 'e':
            return 0
            
    


