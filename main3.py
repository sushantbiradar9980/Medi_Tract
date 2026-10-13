from tkinter import *
import database1

def viewAllPatients():
    win = Toplevel()
    win.title("All Patients List ")
    win.geometry("600x400")

    bg_photo2 =PhotoImage(file="viewAllBackground.png")
    bg_label2 = Label(win,image =bg_photo2)
    bg_label2.place(x =0,y=0,relwidth=1,relheight=1)
    bg_label2.image =bg_photo2

    view1 = Label(win,text="All Patients List ")
    view1.pack(pady =10)

    #Box to display
    listBox = Listbox(win,width=65,height = 12)
    listBox.pack(padx = 10,pady =10)

    records = database1.getPatients()
    for i in records:
        listBox.insert(END,f"ID : {i[0]} Name :{i[1]} Age:{i[2]} Gender: {i[3]} Emergency:{i[4]} Diseases : {i[5]}")

    btn2 =Button(win, text ="Close ",command= win.destroy)
    btn2.pack(pady=10)