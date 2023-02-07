from tkinter import *
from tkinter import messagebox
import webbrowser

window = Tk()
window.geometry('640x800')
window.resizable(False,False)
photo = PhotoImage(file='./git.png')
def security():
    n = entry.get()
    s = entry1.get()
    if len(n) or len(s) == 0:
        messagebox.showerror(title='Error',message='Вы не заполнили одно поле!!!!')
    if len(n) and len(s) != 0:
        webbrowser.open("https://github.com/Qudaybergen09/GitHub")
lbl = Label(image=photo)
lbl.pack(anchor='center')

label = Label(text='Username / email :')
label.place(x=10,y=275)

entry = Entry()
entry.place(x=25,y=300,width=450,height=25)

label = Label(text='Password')
label.place(x=10,y=400)

entry1 = Entry()
entry1.place(x=25,y=425,width=450,height=25)

btn = Button(text='Login',font='Roboto 15',command=security)
btn['bg'] = 'green'
btn['fg'] = 'white'
btn.place(x=225,y=560,width=150,height=30)


window.mainloop()
