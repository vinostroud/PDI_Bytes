WORKOUT_SCHEDULE = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
REST, CHILL_OUT, TRAIN = 'Rest', 'Chill out!', 'Go train {}'
INVALID_DAY = 'Not a valid day'

def get_workout_motd(day):
    day_key = day.title() #this is the search key in title case
        
    if day_key not in WORKOUT_SCHEDULE.keys():  #check if title case key is in the workout schedule dict, if not, return invalid variable 
        return INVALID_DAY
    elif day_key == 'Saturday' or day_key == 'Sunday':  #check the two rest days (literally, I didn't check against a variable which I suspect is inelegant)
        return CHILL_OUT        
    else:
        workout_value = WORKOUT_SCHEDULE[day_key]  #if first two conditions don't return the value, you know the key will return a value
        return TRAIN.format(workout_value)
    

        
print(get_workout_motd('Thursday'))

 






'''steps:
1. Get the day
2. check if day is in WORKOUT_SCHEDULE.keys
3. Make it case insensitive
4. Return result based on day
'''