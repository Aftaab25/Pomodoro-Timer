"""
timer for work:  50*60
timer for break: 10*60

for minutes: timer//60
for seconds: timer%60
"""

import tk

# Let the time left be 1366
timeLeft = 1366             # (in seconds)
minute, second = divmod(timeLeft, 60)
print(minute)
print(second)

print("DONE")