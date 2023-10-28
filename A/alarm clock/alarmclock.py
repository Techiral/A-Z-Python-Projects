import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            frequency = 2500  # Set frequency to 2500 Hz
            duration = 1000  # Set duration to 1000 ms (1 second)
            winsound.Beep(frequency, duration)
            break

if __name__ == "__main__":
    alarm_time = input("Enter the time for the alarm (in HH:MM:SS format): ")
    set_alarm(alarm_time)
