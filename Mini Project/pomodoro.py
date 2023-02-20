#!/usr/bin/python3

import time

def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_second -= 1
    print("Done")

if __name__ == '__main__':
    countdownTimer(25, 0) # 25 minutes
