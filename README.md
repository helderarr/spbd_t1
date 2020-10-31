# spbd_t1
 
| Col# | Column Name          | Type        | Description                                                          |
|------|----------------------|-------------|----------------------------------------------------------------------|
| 1    | Trip ID              | Plain Text  | A unique identifier for the trip.                                    |
|      |                      |             |                                                                      |
| 2    | Taxi ID              | Plain Text  | A unique identifier for the taxi.                                    |
|      |                      |             |                                                                      |
| 3    | Trip Start Timestamp | Date & Time | When the trip started, rounded to the nearest 15 minutes.            |
|      |                      |             |                                                                      |
| 4    | Trip End Timestamp   | Date & Time | When the trip ended, rounded to the nearest 15 minutes.              |
|      |                      |             |                                                                      |
| 5    | Trip Seconds         | Number      | Time of the trip in seconds.                                         |
|      |                      |             |                                                                      |
| 6    | Trip Miles           | Number      | Distance of the trip in miles.                                       |
|      |                      |             |                                                                      |
| 7    | Pickup Region ID     | Plain Text  | The City Region where the trip began. For privacy, this field is not |
|      |                      |             | shown for some trips.                                                |
|      |                      |             |                                                                      |
| 8    | Dropoff Region ID    | Plain Text  | The City Region where the trip ended. For privacy, this field is not |
|      |                      |             | shown for some trips.                                                |
|      |                      |             |                                                                      |
| 9    | Pickup Community     | Number      | The Community Area where the trip began. For privacy, this field     |
|      | Area                 |             | is not shown for some trips.                                         |
|      |                      |             |                                                                      |
| 10   | Dropoff Community    | Number      | The Community Area where the trip ended. For privacy, this field     |
|      | Area                 |             | is not shown for some trips.                                         |
|      |                      |             |                                                                      |
| 11   | Fare                 | Number      | The fare for the trip.                                               |
|      |                      |             |                                                                      |
| 12   | Tips                 | Number      | The tip for the trip.                                                |
|      |                      |             |                                                                      |
| 13   | Tolls                | Number      | The tolls for the trip.                                              |
|      |                      |             |                                                                      |
| 14   | Extras               | Number      | Extra charges for the trip.                                          |
|      |                      |             |                                                                      |
| 15   | Trip Total           | Number      | Total cost of the trip, the total of the previous columns.           |
|      |                      |             |                                                                      |
| 16   | Payment Type         | Plain Text  | Type of payment for the trip.                                        |
|      |                      |             |                                                                      |
| 17   | Company              | Plain Text  | The taxi company.                                                    |
|      |                      |             |                                                                      |
| 18   | Pickup Centroid      | Number      | The latitude of the center of the pickup city region or the          |
|      | Latitude             |             | community area if the city region has been omitted. For privacy,     |
|      |                      |             | this field is not shown for some trips.                              |
|      |                      |             |                                                                      |
| 19   | Pickup Centroid      | Number      | The longitude of the center of the pickup city region or the         |
|      | Longitude            |             | community area if the city region has been omitted. For privacy,     |
|      |                      |             | this field is not shown for some trips.                              |
|      |                      |             |                                                                      |
| 20   | Pickup Centroid      | Point       | The location of the center of the pickup city region or the          |
|      | Location             |             | community area if the city region has been omitted. For privacy,     |
|      |                      |             | this field is not shown for some trips.                              |
| 21   | Dropoff Centroid     | Number      | The latitude of the center of the dropoff city region or the         |
|      | Latitude             |             | community area if the city region has been omitted. For privacy,     |
|      |                      |             | this field is not shown for some trips.                              |
|      |                      |             |                                                                      |
| 22   | Dropoff Centroid     | Number      | The longitude of the center of the dropoff city region or the        |
|      | Longitude            |             | community area if the city region has been omitted. For privacy,     |
|      |                      |             | this field is not shown for some trips.                              |
|      |                      |             |                                                                      |
| 23   | Dropoff Centroid     | Point       | The location of the center of the dropoff city region or the         |
|      | Location             |             | community area if the city region has been omitted. For privacy,     |
|      |                      |             | this field is not shown for some trips.                              |
