from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of the alarm(hh:mm:ss, am/pm) = ")
alarm_hr = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:12].upper()

print ("Setting up alarm of {}:{}:{} {}".format(alarm_hr, alarm_min, alarm_sec, alarm_period))

while True:
    now = datetime.now()
    current_hr = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if (alarm_period == current_period):
        if(alarm_hr == current_hr):
            if(alarm_min == current_min):
                if(alarm_sec==current_sec):
                    print("FBI...FBI...Openup!")
                    playsound('audio.mp3')
                    break
