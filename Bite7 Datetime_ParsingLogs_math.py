from datetime import datetime
from datetime import timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()

'''
line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'
'''

# for you to code:


#This works
def convert_to_datetime(line):
     
    stripped_logline = line.strip().split() #this will remove whitespace (strip) and split() out the date
    the_date = stripped_logline[1] #date is second item, position [1]
    the_datetime = datetime.strptime(the_date, '%Y-%m-%dT%H:%M:%S') #create datetime object
    return the_datetime
'''
#test
print(convert_to_datetime(line1))
print(convert_to_datetime(line2))
print(convert_to_datetime(line3))
'''   


def time_between_shutdowns(loglines):
    #for each_line in loglines:
    shutdown_lines = [line for line in loglines if "shutdown initiated" in line.lower()] #returns list of shutdown initiated lines
    shutdown_line_start = convert_to_datetime(shutdown_lines[0])
    shutdown_line_end = convert_to_datetime(shutdown_lines[-1])
    time_difference = shutdown_line_end - shutdown_line_start
    return time_difference

print(time_between_shutdowns(loglines))
    



'''
time_test = datetime.strptime('2014-07-03 23:27:51', '%Y-%m-%d %H:%M:%S')
print(time_test)
'''




'''     
Notes on ToDo #1:

test_split = "INFO 2014-07-03T23:27:51 supybot Shutdown complete."
split_test_date = test_split.split()
print(split_test_date)

the_date = split_test_date[1]
print(the_date)

test_date_strp = datetime.strptime(the_date, '%Y-%m-%dT%H:%M:%S')
print(test_date_strp)
'''


  
    
'''
TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
'''
    

'''
def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
'''