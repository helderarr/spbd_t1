import pyspark



def get_month(line):
    """ Returns the month from a line"""
    columns = line.split(';')
    start_timestamp = columns[start_timestamp_position - 1]
    start_timestamp = datetime.strptime(start_timestamp, "%m/%d/%Y %I:%M:%S %p")
    return start_timestamp.month


sc = pyspark.SparkContext('local[*]')
try:
    # assign file to context
    lines = sc.textFile('data/Taxi_Trips_151MB.csv')
    # data quality: remove empty lines
    non_empty_lines = lines.filter(lambda line: len(line) > 0)
    # creates pais (month,1) for aggregating months count
    line_months = non_empty_lines.map(lambda line: (get_month(line), 1))
    # applies the aggregation function
    occurrences = line_months.reduceByKey(sum)
    # computes and iterates for all months
    for (k, v) in occurrences.collect():
        print(k, v)

    sc.stop()
except:
    sc.stop()