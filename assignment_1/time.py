def get_hour_mins(fulltime):
	'''Gets time in format HH:MM and returns hour and minutes tuple'''
	return (int(fulltime[0:2]),int(fulltime[3:5]))

def calculate_duration(firsttime,secondtime):
	'''Gets 2 time tuples, returns one tuple of duration -  hour,minutes'''
	# get times from tuples
	firsthour,firstmin = firsttime
	secondhour,secondmin = secondtime
	
	# Calculate normal diff
	hourdiff = secondhour-firsthour
	mindiff = secondmin-firstmin
	# if minutes in later time are smaller, we need to deduct 1 hour and fix minutes diff
	if (mindiff < 0):
		hourdiff -= 1
		mindiff = 60+mindiff
	return hourdiff,mindiff
	
def main():
	fulltimes = input("please enter two times in this format: 16:45-20:20\n")
	firsttime = get_hour_mins(fulltimes[0:5])
	print(firsttime)
	secondtime = get_hour_mins(fulltimes[6:11])
	print(secondtime)
	hourduration,minduration = calculate_duration(firsttime,secondtime)
	print ("Total duration:", hourduration, "hours and", minduration, "minutes")
	

if __name__== "__main__":
	main()