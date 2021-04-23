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
            try:
                dataJSON = json.loads(dataString)

                print(dataJSON['snr[2]']['snrVal'])
                text.insert(END, dataJSON['snr[2]']['snrVal'])
                text.insert(END, '\n')
                text.
                
            except:
                print("ups")
        else:
            pass

if __name__ == "__main__":
    frame_1 = Frame(height=285, width=480,bd=3,relief="groove").place(x=7,y=5)
    frame_2 = Frame(height=150, width=480,bd=3, relief="groove").place(x=7,y=300)
    text = Text(width=59, height=17)
    text.place(x=8,y=6)
    t1 = threading.Thread(target=getUARTdata)
    t1.daemon = True
    t1.start()
    gui.geometry('500x500')
    gui.mainloop()