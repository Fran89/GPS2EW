# GPS2EW
Python class that can be used to transmit info to an Earthworm System via AMQP. This script specifically deals with transmiting
the data to the messaging server and formating it into the correct geojson format. An earthworm module called geojson to EW 
deals with putting it in an tracebuff2 structure and placing it in the message ring.

## Requires
This script has various requirements:

* A script that can pull info such as X, Y, Z and time from a GPS Receiver.
* Python modules: pika, json.
* A configured [earthworm system](http://earthwormcentral.org/).
* A configured AMQP Server, such as [RabbitMQ](https://www.rabbitmq.com/).

## How to:

1. First configure the config.py
  + RABBIT_HOST='localhost' (or Rabbit Host)
  + QUEUE_TOPIC='Results2Earthworm' (is the default, must be the same in the geojson2ew config)
2. In the script that can pull info from the reciever import the GPS-AMQP:
  + Call: variable = GPStoEW("STAT.NET.COMP_.LOC")
  + This setup is important: 
    + 4 letter station name (dot)
    + 2 letter network code (underscore)(dot)
    + 2 letter component (dot)
    + 2 character location
 + The final letter of the component will substitute the underscore in the geojson2ew module
3. Everytime the scripts recieves data
  + Call: variable.sendGPS(Lat,Lon,Ele,Time) (or xyz)
  + Time must be Unix Epoch (seconds since 1970) GMT.
4. Configure geojson2ew.d (An example configuration included)

## Flowchart
![Flowchart](https://github.com/Fran89/GPS2EW/blob/master/img/Flow.svg.png)

### Thanks
* Advisor: Alberto Lopez, for encouring me to create this script.
* The people over at Instrumental Software Technologies, Inc. (ISTI) @ http://www.isti.com/
* Everyone who has ever worked with in the development of earthworm @ http://earthwormcentral.org
