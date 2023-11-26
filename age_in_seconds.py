import os
import time
from datetime import datetime

born_date = input('Enter your birthday (DD-MM-YYYY-HH-MM): ').split('-')
born_date = [int(i) for i in born_date]
year, month, day, hours, minutes = [born_date[i] for i in range(len(born_date))]
born = datetime(day, month, year, hours, minutes)

while True:
    alive = datetime.now() - born
    print(f'You are alive for {int(alive.total_seconds())} seconds!')
    time.sleep(1)
    os.system('cls')
