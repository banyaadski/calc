from datetime import datetime 
from time import time 


def log_create_complex(a, b, c, d, data, operand):
    time = datetime.now().strftime("%H:%M:%S")
    with open('log_journal.csv', 'a') as file:
        file.write(f'{time}: {a}{b} {operand} {c}{d} = {data}\n')
    file.close()

def log_create_rational(a, b, data, operand):
    time = datetime.now().strftime("%H:%M:%S")
    with open('log_journal.csv', 'a') as file:
        file.write(f'{time}: {a} {operand} {b}  = {data}\n')
    file.close()



 



