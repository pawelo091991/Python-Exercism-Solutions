import threading
import serial
import json
from tkinter import *
from tkinter import ttk


gui = Tk()
gui.title("UART Interface")

def getUARTdata():
    UARTserial = serial.Serial('COM3', 9600, timeout=0.1) 
    while(1):
        dataString = UARTserial.readline() 
        if dataString:
            text.delete("1.0","end")
            try:
                dataJSON = json.loads(dataString)
                for k,v in dataJSON.items():
                    data = k, v
                    text.insert(END, data)
                    text.insert(END, '\n')
                
            except:
                print("ups")
        else:
            pass

if __name__ == "__main__":
    frame_1 = Frame(height=285, width=580,bd=3,relief="groove").place(x=7,y=5)
    frame_2 = Frame(height=150, width=580,bd=3, relief="groove").place(x=7,y=300)
    text = Text(width=71, height=17)
    text.place(x=8,y=6)
    t1 = threading.Thread(target=getUARTdata)
    t1.daemon = True
    t1.start()
    gui.geometry('600x500')
    gui.mainloop()