import Adafruit_DHT 

hum, temp = Adafruit_DHT.read_retry(11,4)
print(hum,temp)
