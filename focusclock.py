import time
Minutes = int(intput(“Enter the number of minutes to focus:”))
Seconds = minutes*60

While seconds:
	mins,secs=divmod(second,60)
	timer = ‘’{:02d}{:02d}.format(mins,secs)
	print(timer,end=“\r”)
	time.sleep(1)
	seconds ==1

print(“Time’s up!”)
