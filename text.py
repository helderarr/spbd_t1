
#line = "0f7572c6b0465c8ebd4e54445e7a26a989f8e486;72fa75a736779ba1abb3fee6686254e254956acc5ac5b93964f28aa445a796164c0aa35e18b04d3ed03a6fdc010c86f95d5ac74aa76a7cfe1d3dec74f514c705;03/23/2013 11:30:00 PM;03/23/2013 11:45:00 PM;1,440;17.68;17031980000;;76;;36.25;0.00;0.00;3.00;39.25;Cash;;41.97907082;-87.903039661;POINT (-87.9030396611 41.9790708201);;;"
# import sys
import sys
# import string library function
import string

from datetime import datetime

# Trip Start Timestamp position
start_timestamp_position = 3

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into columns
    columns = line.split(";")

    satart_timestamp = columns[start_timestamp_position - 1]

    date_start = datetime.strptime(satart_timestamp, "%m/%d/%Y %I:%M:%S %p")

    time_str = date_start.strftime("%I %p")

    print('%s\t%s\t%s\t%s' % (time_str, 1, time_str,time_str))

