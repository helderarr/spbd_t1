import sys

total_count = 0
total_trip_miles = 0
total_trip_total = 0
old_key = ""

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    #key, count, trip_miles, trip_total = line.split('\t', 1)
    key, count = line.split('\t', 1)

    # convert count (currently a string) to int
    count = int(count)
    #trip_miles = float(trip_miles)
    #trip_total = float(trip_total)

    if old_key == key:
        # same key just count
        total_count += count
        #total_trip_miles += trip_miles
        #total_trip_total += trip_total
    else:
        if old_key != "":
            print('%s\t%s\t%s\t%s' % (old_key, total_count,total_trip_miles,total_trip_total))
        old_key = key
        total_count = 1
        #total_trip_miles = trip_miles
        #total_trip_total = trip_total
print('%s\t%s\t%s\t%s' % (old_key, total_count,total_trip_miles,total_trip_total))
