import webbrowser
import pyautogui
import time
import sys          
import subprocess
from datetime import datetime
# my help this time: https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python?rq=1
# datetime object containing current date and time
aniversary = datetime(2002, 7, 19, 2, 0, 0)             #You'd have to get your date right!
now = datetime.now()

# dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)	

duration = now - aniversary  

print(duration)
duration_in_s = duration.total_seconds()
years = divmod(duration_in_s, 3.154e+7)       # Get years (without [0]!)
days    = divmod(years[1], 86400)        
hours   = divmod(days[1], 3600)               # Use remainder of days to calc hours
minutes = divmod(hours[1], 60)                # Use remainder of hours to calc minutes
seconds = divmod(minutes[1], 1)               # Use remainder of minutes to calc seconds
# TimeAlive = ("Alive for: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))
TimeAlive = ("Alive for: %d years, %d days, %d hours" % (years[0], days[0], hours[0]))
print (TimeAlive)

url = 'https://www.instagram.com/accounts/edit/'

if sys.platform=='win32':
    subprocess.Popen(['start', url], shell= True)
elif sys.platform=='darwin':
    subprocess.Popen(['open', url])
else:
    subprocess.Popen(['xdg-open', url])

time.sleep(3)

for i in range(0, 17):
    pyautogui.press('Tab')


pyautogui.hotkey ('ctrl', 'End')
pyautogui.hotkey ('shift', 'ctrl', 'home')
pyautogui.write("%s\nWhen I in dreams behold thy fairest shade\nIn them doth wake the sleeping morn\nThe daytime shadow of my love betray'd\nLends night to dreams faded form" % (TimeAlive))

for i in range(0, 6):
    pyautogui.press('Tab')

pyautogui.press ('enter')

time.sleep (0.5)

pyautogui.hotkey ('ctrl', 'w')