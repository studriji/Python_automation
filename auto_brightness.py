import screen_brightness_control as sbc
import schedule

#current_brightness = sbc.get_brightness()
#print(current_brightness)

def morning():
    sbc.set_brightness(100)

def night():
    sbc.set_brightness(20)

#set the time accordingly
schedule.every().day.at('17:11').do(morning)
schedule.every().day.at('17:10').do(night)

while True:
    schedule.run_pending()
