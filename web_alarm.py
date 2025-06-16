import time
import webbrowser

set_alarm = input("Enter alarm : ")

url = input("Enter the web URL : ")

actual_Time = time.strftime("%I:%M:%S")

while(actual_Time != set_alarm):
    print("Not Yet")

if actual_Time == set_alarm:
    webbrowser.open(url)