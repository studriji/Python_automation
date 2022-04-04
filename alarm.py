import time 
import schedule
import winsound
from win10toast import ToastNotifier
from playsound import playsound
#pip install playsound==1.2.2

notify = ToastNotifier()

def alarm():
    print("drink water!!")
    #time.sleep(1)
    playsound('alarm.mp3')
    
    notify.show_toast("REMINDER","Drink Water!!",duration=3)
    #winsound.Beep(400,2000)

#schedule.every(10).seconds.do(alarm)
schedule.every().day.at('22:08').do(alarm)
schedule.every().day.at('22:10').do(alarm)
while True:
    schedule.run_pending()
    #time.sleep(3)

