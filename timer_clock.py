import time
import os
import sys
from datetime import datetime

def timer_clock():
    platform = sys.platform
    command_clear = 'cls' if platform == 'win32' else 'clear'
    while True:
        time_now = datetime.now().strftime('%H:%M:%S')
        print(time_now)
        time.sleep(1)
        os.system(command_clear)

def run():
    timer_clock()

if __name__ == '__main__':
    run()