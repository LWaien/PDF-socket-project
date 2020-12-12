from tkinter import *
from tkinter.filedialog import askopenfilename
import client as c
from datetime import datetime


def send():
    timestamp = datetime.now(tz=None)
    filename = askopenfilename()
    print(filename)
    addr = port.get()
    SERVER, PORT = addr.split(':')
    SERVER = bytes(SERVER, 'utf-8')
    c.file(SERVER, int(PORT), filename)
    info = Label(window, text="file sent to " + addr + ' ' + str(timestamp))
    info.pack()
    window.update()


window = Tk()
window.minsize(300,300)
txt = Label(window,text='Enter server ip as xxx.xxx.xx.xx:port')
txt.pack()
port = Entry(window)
port.pack()
sendbut = Button(window,text='Send File',fg='Blue',command=send)
sendbut.pack()




window.mainloop()

