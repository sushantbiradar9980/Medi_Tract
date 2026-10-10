from tkinter import *
import main2,main3,main4,database1
database1.patient()

top = Tk() #Create window
top.title("Medi Track ")
top.geometry("600x400")

#Image
bg_photo = PhotoImage(file="background.png")
bg_label =Label(top,image=bg_photo)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)
bg_label.image =bg_photo

btn1 = Button(top,text ="Register Patient ",command = main2.registerPatient)
btn1.grid(row = 1,column =0,padx =20,pady =20)

btn2 = Button(top,text = "View All Patients ",command=main3.viewAllPatients)
btn2.grid(row = 3,column =0,padx =20,pady = 20)

btn3 = Button(top,text ="Search Record ",command=main4.searchRecord)
btn3.grid(row = 5,column = 0,padx = 20,pady = 20)

top.mainloop()