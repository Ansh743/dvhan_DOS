import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import re
import Sender
import pyaudio



p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)

sObj = Sender.SenderObj(stream)

status_list = ['green','orange','red']
global i 
i = 0
def status(st, r):
    global i 
    i = st
    light = ImageTk.PhotoImage(Image.open("gui_components/"+status_list[i]+".jpg"))
    lbl = ttk.Label( image=light,background = 'white')
    lbl.image = light
    lbl.place(x=225, y=451)
    

def recieve():
    #status update to processing
	# TODO: Connect backend
    None

def transmit():
    #status update to processing
    global i
    i = 1
    status(i,r=root)
    bits = text_box.get()
    p = re.compile('^[0-1]*$')
    m = p.match(bits)
    
    if m and len(bits) != 0:
        print('Working')
        sObj.send(msg=bits)
        
    else:
        print('Enter Valid binary text')
    
        
    i = 0
    status(i, r = root)
    
    
    

root = tk.Tk()
root.title('Dvhan v1.0')

root.geometry("1000x550")
root.configure(bg="white")


s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 12))

p1 = '''· Enter the text data in the field below and press Send to trasmit it.'''
p2 = '''· Press on receive to listen for data being trasmitted by another Dvhan application.'''
p3 = 'Status:'

myLabel1 = ttk.Label(root, text=p1, background='white', font=(20))
myLabel2 = ttk.Label(root, text=p2, background='white',font=(20))
myLabel3 = ttk.Label(root, text=p3, background='white',font=(30))

myLabel1.place(x=260, y=85)
myLabel2.place(x=260, y=150)
myLabel3.place(x=150, y=450)


render = ImageTk.PhotoImage(Image.open("gui_components/info.jpg"))
info = ttk.Label(image=render,background = 'white')
info.image = render
info.place(x=430, y=425)

render = ImageTk.PhotoImage(Image.open("gui_components/dvhan_logo.jpg"))
logo = ttk.Label(image=render,background = 'white')
logo.image = render
logo.place(x=70, y=20)

status(i,r=root)


send_button = ttk.Button(
    root,
    text='Send',
    style='my.TButton',
    command = transmit,
    
)
send_button.pack(
    ipadx=100,
    ipady=40,
    expand=True
)
text_box=ttk.Entry(justify= 'center', font=(25))

recieve_button = ttk.Button(
    root,
    text='Receive',
    style='my.TButton',
    command = recieve,
    
)
recieve_button.pack(
    ipadx=65,
    ipady=12.66,

    expand=True
)

text_box.pack(
    padx=10
)

send_button.place(y=270, x=700,height=40,width=200,)
recieve_button.place(y=340, x=700,height=40,width=200)
text_box.place(x=90, y=250,height=150, width=550)


root.resizable(False, False)


root.mainloop()