import paho.mqtt.client as mqtt
import thread,time
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
lastmsg = [0,0]
test = 1
# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
     
    out = msg.payload
    #print out
    #test = out
    #print test
    out = out.split(" ")
    out = out[0] + ","+ out[1]
    f = open("data.txt","w")
    #f.write(out)
    #f.close()  
    #print out
   # out = out.split(' ')
   
    #lastmsg[0] = out[0]
    #lastmsg[1] = out[1]
    f.write(out)
    f.close()
    print out
    #print lastmsg
#    return lastmsg


    #print lastmsg
    #print int(out[1][1:], int(cout[1][1:]))

    #beyop = str(msg.payload)
    #beyop = beyop.split(" ")
    #lastmsg = [int(beyop[0]), int(beyop[1])]
    #print lastmsg + "aa"
    # more callbacks, etc

def angle():
    return lastmsg

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)
 
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
client.loop_forever()

    
