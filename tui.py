import time
import sys
import argparse
import os

def pomodoro_timer(minutes):
    try:
        seconds = minutes * 60
        print(f"Pomodoro started for {minutes} minutes. Stay focused!")
        
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f'{mins:02}:{secs:02}'
            print(f'\rTime left: {timer}', end='')
            time.sleep(1)
            seconds -= 1
        
        print("\nTime's up! Take a break.")
        
        # Optional: Play a sound when the timer ends (requires 'ffplay')
        # if os.name == 'posix':
        #     subprocess.run(['ffplay', '-nodisp', '-autoexit', '/usr/share/sounds/freedesktop/stereo/complete.oga'])
        # else:
        #     print('\a')  # For Windows or other platforms, this will just make a beep sound
    
    except KeyboardInterrupt:
        print("\nTimer interrupted. Take a short break!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pomodoro Timer')
    parser.add_argument('minutes', type=int, help='Duration of the Pomodoro session in minutes')
    args = parser.parse_args()
    
    pomodoro_timer(args.minutes)

