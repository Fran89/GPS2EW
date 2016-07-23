#!/usr/bin/env python
import pika
import json  
import config as cfg 

class GPStoEW:
	
	#Let's initialize
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
	channel    = connection.channel() 
	channel.queue_declare(queue=cfg.QUEUE_TOPIC) 
        SNCL = ""
        
	#Init class
	def __init__(self, StaSNCL = "TEST.XX.GP_.--"):
		self.SNCL = StaSNCL
		return

	# Send GPS Info Function
	def sendGPS(self, NS = "125.6", EW = "10.1",UD = "10", TM = "3100000000"):
		data = 	{
			"type": "FeatureCollection",
			"properties": {
				"coordinateType": "NEU",
				"SNCL": self.SNCL,
				"time": float(TM),
				"sampleRate": 1
			},
			"features": [{
			  "type": "Feature",
				"geometry": {
					"type": "Point",
					"coordinates": [NS, EW, UD]
				},
				"properties": {
					"quality": 9,
					"EError": 1,
					"NError": 1,
					"Error": 1,
					"ENCovar": 1,
					"EUCovar": 1,
					"NUCovar": 1
				}
			}]
		}
		message = json.dumps(data,indent=4,ensure_ascii=False)
		message += "}"
		self.channel.basic_publish(exchange='', routing_key=cfg.QUEUE_TOPIC, body=message)
		print(" [x] Sent data to RabbitMQ")
		return

	# Close connection
	def closeGPS():
		self.connection.close()
		return

#test=GPStoEW("GPS2.PR.GP_.--")
#test.sendGPS(19 -72,10 )

