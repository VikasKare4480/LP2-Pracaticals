#pip install tkinter
from tkinter import *
root = Tk()
root.title("ChatBot")
def send():
    send = "You -> "e.get()
    txt.insert(END, "\n" + send)
    user = e.get().lower()
    if(user == "Hello"):
        txt.insert(END, "\n" + "Bot -> Hello World I am Chatbot, Speed 1 terahertz")
    elif(user == "hi" or user == "hii" or user == "hiii"):
        txt.insert(END, "\n" + "Bot -> Hello")
    elif(e.get() == "How are you"):
        txt.insert(END, "\n" + "Bot -> Fine & You")
    elif(user == "Fine" or user == "Good" or user == "I am Doing Good"):
        txt.insert(END, "\n" + "Bot -> Great, HOw can I help ya")
    elif(e.get() == "how to make chatbot"):
        txt.insert(END, "\n" + "Bot -> Search on Google")
    else:
        txt.insert(END, '\n' + "Bot -> Sorry! I didn't get you")
    e.delete(0, END)

txt = Text(root)
txt.grid(row = 0, column = 0, columnspan = 2)
e = Entry(root, width = 100)
e.grid(row = 1, column = 100)
send = Button(root, text = "Send", command = send).grid(row = 1, column = 1)
roo