import serial
import json

def serialUART():
    UARTserial = serial.Serial('COM3', 9600, timeout=0.1) 
    dataString = UARTserial.readline() 
        if data:
            dataString = data.decode()
            return json.loads(data)
        else:
            return None
        