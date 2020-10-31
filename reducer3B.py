import sys

counter=0
n=5
old_hour = ""

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, full_hour, out_key, count, trip_miles, trip_total = line.split(';', 5)

    if counter == n:
        if old_hour == full_hour:
            continue
        else:
            counter = 0
            old_hour = full_hour

    old_hour = full_hour
    counter = counter + 1
    print(out_key,count,trip_miles, trip_total)

