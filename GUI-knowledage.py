from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title("โปรแกรมบันทึกข้อมูล")
GUI.geometry("500x400")

L1 = Label(GUI,text="โปรแกรมบันทึกความรู้",font=("Angsana New",30),fg="green")
L1.place(x=30,y=20)

def Button1():
    text = "ตอนนี้มีเงินในบัญชีอยู่ 300 บาท"
    messagebox.showinfo("เงินในบัญชี",text)

FB1 = Frame(GUI)
FB1.place(x=100,y=80)

B1 = ttk.Button(FB1,text="มีเงินอยู่กี่บาท",command=Button1)
B1.pack(ipadx=20,ipady=20)

def Button2():
    text = "Python 101, Math"
    messagebox.showinfo("วิชาเรียนวันที่ 10-20 ก.พ.",text)

FB2 = Frame(GUI)
FB2.place(x=100,y=180)

B2 = ttk.Button(FB2,text="สัปดาห์นี้เรียนวิชาอะไร",command=Button2)
B2.pack(ipadx=20,ipady=20)


GUI.mainloop()

