from tkinter import *
from tkinter.messagebox import showinfo

sc=Tk()
sc.geometry("600x200")
sc.title("Sorathiya Convert")

def From_KG():
    user=User_enter.get()

    if user=="":
        showinfo("Error","Plz Enter a Value")


    gram=float(User_enter.get())*1000
    pound=float(User_enter.get())*2.20462
    ounce=float(User_enter.get())*35.274
    MilliGram=float(User_enter.get())*1e+6
    Ston=float(User_enter.get())*0.157473
    Microgram=float(User_enter.get())*1e+9
    US_ton=float(User_enter.get())*0.00110231

    t1.delete (1.0 , END)
    t1.insert (END,gram)

    t2.delete (1.0 , END)
    t2.insert (END,pound)

    t3.delete (1.0 , END)
    t3.insert (END,ounce)

    t4.delete (1.0 , END)
    t4.insert (END , MilliGram)

    t5.delete (1.0 , END)
    t5.insert (END , Ston)

    t6.delete (1.0 , END)
    t6.insert (END , Microgram)

    t7.delete (1.0 , END)
    t7.insert (END , US_ton)

def All_clear():
    s2.delete(0,END)
    t1.delete(1.0,END)
    t2.delete(1.0,END)
    t3.delete(1.0,END)
    t4.delete(1.0,END)
    t5.delete(1.0,END)
    t6.delete(1.0,END)
    t7.delete(1.0,END)

s1=Label(sc,text = "Enter a KG Value",font="Arial 15 bold")
User_enter=StringVar()
s2=Entry(sc,textvariable = User_enter,width = 20 ,font="Arial 12")
s3=Label(sc,text = "Gram",font="Arial 11 bold")
s4=Label(sc,text = "Pound",font="Arial 11 bold")
s5=Label(sc,text = "Ounce",font="Arial 11 bold")
s6=Label(sc,text = "MilliGram",font="Arial 11 bold")
s7=Label(sc,text = "Ston",font="Arial 11 bold")
s8=Label(sc,text = "Microgram",font="Arial 11 bold")
s9=Label(sc,text = "US_ton",font="Arial 11 bold")


t1=Text(sc,height = 1,width = 20 ,font="Arial 10")
t2=Text(sc,height = 1,width = 20,font="Arial 10")
t3=Text(sc,height = 1,width = 20,font="Arial 10")
t4=Text(sc,height = 1,width = 20,font="Arial 10")
t5=Text(sc,height = 1,width = 20,font="Arial 10")
t6=Text(sc,height = 1,width = 20,font="Arial 10")
t7=Text(sc,height = 1,width = 20,font="Arial 10")

b1=Button(sc,text = "Convert",command = From_KG,font="Arial 11 bold")
b2=Button(sc,text = "Clear",command = All_clear,font="Arial 11 bold")


s1.grid(row = 5,column = 0)
s2.grid(row = 5,column = 1)

b1.grid(row = 5,column = 2)
b2.grid(row = 13,column = 2)

s3.grid(row = 7,column = 0)
s4.grid(row = 7,column = 1)
s5.grid(row = 7,column = 2)

t1.grid(row = 8,column = 0)
t2.grid(row = 8,column = 1)
t3.grid(row = 8,column = 2)

s6.grid(row = 10,column = 0)
s7.grid(row = 10,column = 1)
s8.grid(row = 10,column = 2)

t4.grid(row = 11,column = 0)
t5.grid(row = 11,column = 1)
t6.grid(row = 11,column = 2)

s9.grid(row = 12,column = 0)
t7.grid(row = 13,column = 0)

sc.mainloop()