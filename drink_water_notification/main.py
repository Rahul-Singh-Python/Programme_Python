import time
from plyer import notification

if __name__ == '__main__':
	while True:
		notification.notify(
				title ="Please Drink Water...",
				message ="How much water should you drink a day? You probably know that, it's important to drink plenty of fluids when the temperatures soar outside. But staying hydrated is a daily",
				app_icon = "/home/rahul/newproject/geeky/practice/drink_water_notification/water.ico",
				timeout= 10
		)
		time.sleep(60*60)



# pythonw main.py