import time

duration = int(input("Enter the timer duration in seconds: "))

for remaining in range(duration, 0, -1):
    print(f"Time remaining: {remaining} seconds")
    time.sleep(1)

print("Time's up!")
