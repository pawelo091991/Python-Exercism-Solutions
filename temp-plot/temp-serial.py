from socket import timeout
import serial
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime as dt


def getUARTdata():
    UARTserial = serial.Serial('COM3', 9600, timeout=0.1)
    while(1):
        if datastring := UARTserial.readline():
            return(float(str(datastring)[2:6]))
        

if __name__ == "__main__":
    plt.style.use("fast")
    time_now = dt.datetime.now()
    x_vals = []
    y_vals = []
    y_mean = [0] * 300
    y_vals_mean = []
    iter = 0

    def animate(i):
        global iter
        temp = getUARTdata()
        x_vals.append(dt.datetime.now())
        y_vals.append(temp)
        y_mean[iter] = temp
        y_vals_mean.append(sum(y_mean)/300)
        iter += 1
        iter %= 300
        
        plt.cla()
        plt.plot(x_vals, y_vals)
        plt.plot(x_vals, y_vals_mean)
        plt.title(f"Current temp: {temp}$^\circ$C\nTime: {str(dt.datetime.now() - time_now)[0:7]}")
        plt.xlabel("Time")
        plt.ylabel("Temp")
        


    ani = FuncAnimation(plt.gcf(),animate,interval=500)

    plt.tight_layout()

    plt.show()