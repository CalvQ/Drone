import paho.mqtt.publish as publish
import serial, time, math
MQTT_SERVER = "192.168.34.195"
MQTT_PATH = "test_channel"
ser = serial.Serial('/dev/ttyACM1',115200,timeout=1)
t = time.time()
#while(True):
#    publish.single(MQTT_PATH, "Hello", hostname=MQTT_SERVER)

while(True):
    if(time.time()-t<5):
        line = ser.readline()
        continue
    
    time.sleep(0.1) 
    #publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)
    line = ser.readline()
    if(line == ""):
        continue
    line = line.split("\t")
    for i in range(3):
        if(line[i] == ''):
            continue
    #print line
    Acceleration_angle = [0,0]
    #print int(line[1])/16384.0
    #print line
    Acceleration_angle[0] = math.atan((int(line[2]))/math.sqrt(pow(int(line[1]),2) + pow(int(line[3]),2)))*180/3.141592654;
    Acceleration_angle[1] = math.atan(-1*int(line[1])/math.sqrt(pow(int(line[2]),2) + pow(int(line[3]),2)))*180/3.141592654;
    out = str(Acceleration_angle[0])+" "+str(Acceleration_angle[1])
    
    print Acceleration_angle
    publish.single(MQTT_PATH, out, hostname=MQTT_SERVER)

    
