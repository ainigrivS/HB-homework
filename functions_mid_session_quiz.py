def convert_to_seconds(hours, minutes, seconds):
	
	hours_to_minutes = hours * 60
	allminutes_to_convert= hours_to_minutes + minutes
	hoursminutes_to_seconds = allminutes_to_convert * 60
	total_seconds = hoursminutes_to_seconds + seconds	

	return total_seconds

total_time_sec = convert_to_seconds(1, 1, 1)
print total_time_sec


def convert_to_inches(feet, inches):
	feet_to_inches = feet * 12
	total_inches = feet_to_inches + inches	

	return total_inches

totalinches = convert_to_inches(1, 1)
print totalinches 
