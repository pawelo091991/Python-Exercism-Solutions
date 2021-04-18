import time
import threading
from tkinter import *
from tkinter import ttk
import serial

serial_data = ''
filter_data = ''
update_period = 5
serial_object = None
gui = Tk()
gui.title("UART Interface")


def connect():
    version_ = button_var.get()
    print(version_)
    global serial_object
    port = port_entry.get()
    baud = baud_entry.get()

    try:
        if version_ == 2:
            try:
                serial_object = serial.Serial("COM3", baud)
            except:
                print("Cant Open Specified Port")
        elif version_ == 1:
            serial_object = serial.Serial("COM3", baud)

    except ValueError:
        print("Enter Baud and Port")
        return
    
    t1 = threading.Thread(target = get_data)
    t1.daemon = True
    t1.start()


def get_data():
    global serial_object
    global filter_data
    while(1):
        try:
            serial_data = serial_object.readline().strip('\n').strip('\r')
            filter_data = serial_data.split(',')
            print(filter_data)

        except TypeError:
            pass


def update_gui():
    global filter_data
    global update_period

    text.place(x=15,y=10)
    progress_1.place(x=60, y=130)
    progress_2.place(x=60, y=160)
    progress_3.place(x=60, y=190)
    progress_4.place(x=60, y=220)
    new = time.time()

    while(1):
        if filter_data:
            text.insert(END, filter_data)
            text.insert(END, "\n")
            try:
                progress_1["value"] = filter_data[0]
                progress_2["value"] = filter_data[1]
                progress_3["value"] = filter_data[2]
                progress_4["value"] = filter_data[3]
                progress_5["value"] = filter_data[4]
            except:
                pass

            if time.time() - new >= update_period:
                text.delete("1.0", END)
                progress_1["value"] = 0
                progress_2["value"] = 0
                progress_3["value"] = 0
                progress_4["value"] = 0
                progress_5["value"] = 0
                new = time.time()

def send():
    send_data = data_entry.get()
    if not send_data:
        print("Sent Nothing")

def disconnect():
    try:
        serial_object.close()

    except AttributeError:
        print("Closed without using it -_-")
    
    gui.quit()


if __name__ == "__main__":
    frame_1 = Frame(height=285, width=480,bd=3,relief="groove").place(x=7,y=5)
    frame_2 = Frame(height=150, width=480,bd=3, relief="groove").place(x=7,y=300)
    text = Text(width=57, height=5)

    t2 = threading.Thread(target=update_gui)
    t2.daemon  = True
    t2.start()

    data1_ = Label(text="Data1:").place(x=15,y=100)
    data2_ = Label(text="Data2:").place(x=15,y=130)
    data3_ = Label(text="Data3:").place(x=15,y=160)
    data4_ = Label(text="Data4:").place(x=15,y=190)
    data5_ = Label(text="Data5:").place(x=15,y=220)

    baud = Label(text="Baud").place(x=100,y=348)
    port = Label(text="Port").place(x=200,y=348)

    progress_1 = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 200, max = 255)
    progress_2 = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 200, max = 255)
    progress_3 = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 200, max = 255)
    progress_4 = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 200, max = 255)
    progress_5 = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 200, max = 255)
    

    data_entry = Entry()
    data_entry.place(x=100,y=255)

    baud_entry = Entry(width=7)
    baud_entry.place(x=100,y=365)

    port_entry = Entry(width=7)
    port_entry.place(x=200,y=365)

    button_var = IntVar()
    radio_1 = Radiobutton(text="Windows", variable=button_var, value=1).place(x=10,y=315)
    radio_2 = Radiobutton(text="Linux", variable=button_var, value=2).place(x=110,y=315)

    button1 = Button(text="Send", command=send, width=6).place(x=15,y=250)
    connect = Button(text="Connect", command = connect).place(x=15,y=360)
    disconnect = Button(text="Disconnect", command=disconnect).place(x=300,y=360)

    gui.geometry('500x500')
    gui.mainloop()

