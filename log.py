from datetime import datetime
import logging
import time


def log_create(x, y, data, operand):
    log = open('log_journal.txt', 'a')
    today = datetime.today()
    log.writelines(f'{today.strftime("%H:%M:%S")}: {x} {operand} {y} = {data}\n')
    log.close()


 



