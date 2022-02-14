from datetime import datetime 
from time import time 


def log_create_complex(a, b, c, d, data, operand):
    time = datetime.now().strftime("%H:%M:%S")
    with open('log_journal.csv', 'a') as file:
        e = '+'
        g = '+'
        if b < 0:
            e = ''
        if d < 0:
            g = ''
        file.write(f'{time}: ({a}{e}{b}j) {operand} ({c}{g}{d}j) = {data}\n')
    file.close()

def log_create_rational(a, b, data, operand):
    time = datetime.now().strftime("%H:%M:%S")
    with open('log_journal.csv', 'a') as file:
        file.write(f'{time}: {a} {operand} {b}  = {data}\n')
    file.close()



 



