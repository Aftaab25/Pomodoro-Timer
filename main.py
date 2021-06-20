# importing the time module
import time

# the countdown function
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Hey time to get up and take a break!")


# input time (in seconds)
t = input("Enter the time in seconds: ")

countdown(int(t))
