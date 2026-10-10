from tkinter import *
from tkinter import messagebox
import database1

def searchRecord():
    win = Toplevel()
    win.title("Search Record ")
    win.geometry("600x400")

    bg_photo3 =PhotoImage(file="viewAllBackground1.png")
    bg_label3 = Label(win,image =bg_photo3)
    bg_label3.place(x =0,y=0,relwidth=1,relheight=1)
    bg_label3.image =bg_photo3

#name
    pa_name =Label(win,text ="Enter Patient's name :")
    pa_name.grid(row=0,column=0,padx=10,pady =10)
    search1 =Entry(win)
    search1.grid(row =0,column=1,padx=10,pady =5)

#age
    pa_age =Label(win,text ="Age :")
    pa_age.grid(row=1,column=0,padx=10,pady =10)
    search2 =Entry(win)
    search2.grid(row =1,column=1,padx=10,pady =5)

#diseases
    pa_dis =Label(win,text ="Disease :")
    pa_dis.grid(row=2,column=0,padx=10,pady =10)
    search3 =Text(win,width =20,height = 4)
    search3.grid(row =2,column=1,padx=10,pady =5)

    def find():
        name =search1.get().strip()
        data = database1.searchPatients(name)
        if(data):
            search2.delete(0,END)
            search2.insert(0,data[2])
            search3.delete("1.0",END)
            search3.insert("1.0",data[4])
            messagebox.showinfo("Found",f"Patient {name} Found")
        else:
            messagebox.showinfo("Error","Patient Not Found")

    def update():
        name =search1.get().strip()
        new_age= search2.get().strip()
        new_disease = search3.get("1.0","end-1c").strip()

        if name =="" or new_age =="" or new_disease=="":
            messagebox.showinfo("Warning","Search first")
            return

        database1.updateDetails(name,new_age,new_disease)
        messagebox.showinfo("Success","Records Updated")
        win.destroy()

    btn_search =Button(win,text ="Search",command =find)
    btn_search.grid(row =0,column=2,padx =10)

    btn_update =Button(win,text ="Update",command =update)
    btn_update.grid(row=3,column=1,pady =20)