# import sys
import sys
# import string library function
import string

from datetime import datetime

# Trip Start Timestamp position
start_timestamp_position = 3

# TripMiles Distance of the trip in miles.
trip_miles_position = 6

# Trip Total - Total cost of the trip, the total of the previous columns.
trip_total_position = 15

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into columns
    columns = line.split(";")

    start_timestamp = columns[start_timestamp_position - 1]
    trip_miles = columns[trip_miles_position - 1]
    trip_total = columns[trip_total_position - 1]

    date_start = datetime.strptime(start_timestamp, "%m/%d/%Y %I:%M:%S %p")

    time_str = date_start.strftime("%I %p")


    #print('%s\t%s\t%s\t%s' % (time_str, 1,trip_miles,trip_total ))
    print('%s\t%s' % (time_str, 1))