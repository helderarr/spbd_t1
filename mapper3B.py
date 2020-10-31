# import sys
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into columns
    time_trip,count,trip_miles, trip_total = line.split("\t")

    hour, half, trip = line.split(" ",2)

    order = 10000000000-int(count)
    
    key = '%s %s %s' % (hour, half, "{:010d}".format(order))

    full_hour = '%s %s' % (hour, half)

    print('%s\t%s\t%s\t%s\t%s\t%s' % (key, full_hour, time_trip, count, trip_miles, trip_total))