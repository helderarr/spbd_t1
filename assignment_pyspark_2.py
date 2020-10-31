import pyspark

pickup_location_position = 7
dropoff_location_position = 8


def get_pickup_dropoff_pairs(line):
    """ Returns the month from a line"""
    columns = line.split(';')
    pickup_location = columns[pickup_location_position - 1]
    dropoff_location = columns[dropoff_location_position - 1]
    return (pickup_location, dropoff_location)


sc = pyspark.SparkContext('local[*]')
try:
    # assign file to context
    lines = sc.textFile('data/Taxi_Trips_151MB.csv')
    # data quality: remove empty lines
    non_empty_lines = lines.filter(lambda line: len(line) > 0)
    # obtain pickup dropoff pairs
    pickup_dropoff_pairs = non_empty_lines.map(lambda line: (get_pickup_dropoff_pairs(line)))
    # remove duplicate pairs
    distinct_pairs = pickup_dropoff_pairs.distinct()
    # remove inconsistent data
    non_empty_distinct_pairs = distinct_pairs.filter(lambda pair:  len(pair[0]) > 0 and len(pair[1]) > 0)
    # group dropoff locations by pickup locations
    pickup_dropoff_pairs = non_empty_distinct_pairs.groupByKey()
    # computes and iterates for all pickup locations
    for pickup, dropoffs in pickup_dropoff_pairs.collect():
        print(pickup, dropoffs.data)

    sc.stop()
except:
    sc.stop()
