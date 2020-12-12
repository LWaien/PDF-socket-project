from tkinter import *
import main as s
from datetime import datetime
import socket

SERVER = socket.gethostbyname(socket.gethostname())

def startserver():
    PORT = port.get()
    info = Label(window, text='Listening...')
    if PORT == '':
        info = Label(window, text='please enter a port')
    info.pack()
    window.update()
    s.start(int(PORT))
    info.destroy()
    timestamp = datetime.now(tz=None)
    info = Label(window, text='File recieved '+'['+str(timestamp)+']')
    info.pack()
    window.update()

window = Tk()
window.minsize(300,300)
txt = Label(window,text='Enter a port to listen on')
txt.pack()
port = Entry(window)
port.pack()
txt2 = Label(window,text='Your server address will be ['+str(SERVER)+':PORT]')
txt2.pack()
but = Button(window,text='Listen for file',fg='Blue',command= startserver)
but.pack()



window.mainloop()


