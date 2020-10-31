import pyspark
from operator import add as sum
from datetime import datetime

# Trip Start Timestamp position
start_timestamp_position = 3
trip_seconds_position = 5
trip_miles_position = 6
pickup_location_position = 7


def get_line_data(line):
    """ Returns the month from a line"""
    columns = line.split(';')
    start_timestamp = columns[start_timestamp_position - 1]
    start_timestamp = datetime.strptime(start_timestamp, "%m/%d/%Y %I:%M:%S %p")
    trip_seconds = columns[trip_seconds_position - 1].replace(",", "")
    trip_miles = columns[trip_miles_position - 1].replace(",", "")
    pickup_location = columns[pickup_location_position - 1]
    # 17031281900_3_12PM
    key = "{}_{}_{}".format(
        pickup_location,
        start_timestamp.weekday(),
        start_timestamp.strftime("%I%p"))

    return (key, (trip_seconds, trip_miles))


def is_line_data_valid(elem):
    # key not empty / Start position exists / trip_seconds not empty / trip_miles not empty
    return len(elem[0]) > 0 and (not elem[0].startswith("_")) \
           and len(elem[1][0]) > 0 and len(elem[1][1]) > 0


def convert_data(elem):
    return elem[0], (int(elem[1][0]), float(elem[1][1]), 1)


# Defining Sequential Operation and Combiner Operations
# Sequence operation : sums tuple
def seq_op(accumulator, element):
    # a little bit of design by contract can help debugging the infrastructure
    # assert allows to define invariants
    assert isinstance(element[0], int)
    assert isinstance(element[1], float)
    assert isinstance(element[2], int)
    return tuple(map(sum, accumulator, element))


# Combiner Operation : sums tuple
def comb_op(accumulator1, accumulator2):
    return tuple(map(sum, accumulator1, accumulator2))


sc = pyspark.SparkContext('local[*]')
try:
    # assign file to context
    lines = sc.textFile('data/Taxi_Trips_151MB.csv')
    # data quality: remove empty lines
    non_empty_lines = lines.filter(lambda line: len(line) > 0)
    # obtain pickup dropoff pairs
    data = non_empty_lines.map(lambda line: (get_line_data(line)))
    data = data.filter(lambda elem: is_line_data_valid(elem))
    data = data.map(lambda elem: convert_data(elem))

    zero_val = (0, 0.0, 0)
    data = data.aggregateByKey(zero_val, seq_op, comb_op)

    data = data.map(lambda elem: (elem[0], (elem[1][0] / elem[1][2], elem[1][1] / elem[1][2])))

    # computes and iterates for all pickup locations
    for k, v in data.collect():
        # key / avg trip_seconds / avg trip_miles
        print(k, "{:0.2f}".format(v[0]), "{:0.2f}".format(v[1]))

    sc.stop()
except Exception as e:
    print(e)
    sc.stop()
