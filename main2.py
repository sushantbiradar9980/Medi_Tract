from tkinter import *
from tkinter import messagebox
import database1

def registerPatient():
    win = Toplevel()
    win.title("Register Patient ")
    win.geometry("600x400")

    bg_photo1 = PhotoImage(file="reg_background.png")
    bg_label1 = Label(win,image= bg_photo1)
    bg_label1.place(x=0,y=0,relwidth=1,relheight=1)
    bg_label1.image = bg_photo1

    #For Name
    name = Label(win,text ="Patient's Name :")
    name.grid(row =0,column =0,padx =10,pady =10)
    p1 =Entry(win)
    p1.grid(row = 0,column =1,padx =10,pady =10)

    #For Age
    age = Label(win,text =" Age :")
    age.grid(row =1,column =0,padx = 10,pady=10)
    p2 =Entry(win)
    p2.grid(row = 1,column = 1,padx =10,pady=10)

    #For Gender
    gend =Label(win,text="Gender :")
    gend.grid(row =2,column =0,padx=10,pady =10)

    gender_var = StringVar(value ="Male")
    gen1 = Radiobutton(win,text ="Male ",variable=gender_var,value ="Male")
    gen1.grid(row =2,column =1)

    gen2 =Radiobutton(win,text ="Female ",variable=gender_var,value="Female")
    gen2.grid(row =2,column =2)

    #Emergency
    emer = Label(win,text ="Emergency")
    emer.grid(row =3,column =0,padx=10,pady=10)

    emer_var =StringVar(value="Nooo")
    emer1 =Radiobutton(win,text ="Yesss",variable=emer_var,value="Yesss")
    emer1.grid(row=3,column=1)

    emer2 =Radiobutton(win,text ="Nooo",variable=emer_var,value="Nooo")
    emer2.grid(row=3,column=2)

    #for Diseases
    dise = Label(win,text ="Diseases : ")
    dise.grid(row =4,column=0,padx =10,pady =10)
    disTxt = Text(win,width =20,height = 4)
    disTxt.grid(row =4,column =1,columnspan=2,padx =10,pady =10)

    # Get Values
    def saveData():
        p_name =p1.get()
        p_age = p2.get()
        p_gend = gender_var.get()
        p_emer =emer_var.get()
        p_disease =disTxt.get("1.0","end-1c").strip()

        if p_name =="":
            messagebox.showwarning("Warning !!!!! ","Enter Name !")
            #messagebox.showwarning("Please enter a name !")
            return

        database1.addPatients(p_name,p_age,p_gend,p_emer,p_disease)
        messagebox.showinfo("Successfully Registered",f"Patient's Name :{p_name}\n Age : {p_age}\n Gender : {p_gend}\n Emergency :{p_emer}\n Disease : {p_disease}")
        win.destroy()

    #Submit
    btn = Button(win,text ="Submit ",command =saveData)
    btn.grid(row =5,column=1,columnspan=2,pady =20)

