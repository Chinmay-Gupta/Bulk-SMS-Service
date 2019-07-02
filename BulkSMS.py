import tkinter
from tkinter import *
import tkinter.messagebox
import os

window=tkinter.Tk()
window.title("Bulk SMS Sender")
window.config(width=640, height=480)

#Select Batch Label
batchSelectLabel = tkinter.Label(window, text="Select Batch")
batchSelectLabel.pack()
batchSelectLabel.place(height=50, relx=0.1)

#Batch Select ListBox
batchSelect = tkinter.Listbox(window)
batchSelect.insert(1,"2017")
batchSelect.insert(2,"2018")

batchSelect.pack()
batchSelect.place(height=80, relx=0.1, rely=0.1, width=200)

#Send Text Label
textLabel=tkinter.Label(window, text="Type SMS Message")
textLabel.pack()
textLabel.place(relx=0.1, rely=0.4)

#SMS Message Body
TextArea = Text(window)
ScrollBar = Scrollbar(TextArea)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set)
ScrollBar.pack(side=RIGHT, fill=Y)
TextArea.pack()
TextArea.place(height=200, width=500, relx=0.1, rely=0.45)

#Method to send SMS text message
def sendSMS():
    batch = open("0","r")
    contacts = str((batch.read()))
    message=TextArea.get("1.0","end-1c")
    batch.close()
    #ENCODE URL HERE !!

    print(contacts)
    print(message)

    tkinter.messagebox.showinfo("Success", "SMS Request sent")
    os._exit(0)




#Send Button
sendBtn=Button(window, text="Send SMS", command=lambda:sendSMS())
sendBtn.pack()
sendBtn.place(height=50, width=200, relx=0.6, rely=0.2)


window.mainloop()