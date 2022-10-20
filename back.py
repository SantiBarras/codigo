
from tkinter import *


def menu():
    ScrumP=Tk()
    ScrumP.title("Scrum Alliance")
    ScrumP.geometry("980x550")
    
    ScrumP.config(bg="#E0E2EE")
    morado=Frame(ScrumP)
    morado.pack(anchor="n")
    morado.config(bg="#6C13E7", width=980,height=85)

    morado1=Frame(ScrumP)
    morado1.pack(side="left")
    morado1.config(bg="#6C13E7", width=121,height=980)

    imagen1=PhotoImage(file="Logo.png")
    esqui1=Label(ScrumP,image=imagen1).place(x=480 , y= 15)

    def destry1():
        ScrumP.destroy()
 
    back=PhotoImage(file="back.png")
    julian3=Button(ScrumP,image=back,bg="#6C13E7",command=destry1).place(x=890 , y= 20)


    boton1=Button(ScrumP, text="ScrumBoard", font=("Arial",12), bg="#6C13E7", width=11).place(x=5 , y= 180)
    boton2=Button(ScrumP, text="To Do", font=("Arial",12), bg="#6C13E7", width=11).place(x=5 , y= 220)
    boton3=Button(ScrumP, text="In Progress", font=("Arial",12), bg="#6C13E7", width=11).place(x=5 , y= 260)
    boton4=Button(ScrumP, text="Done", font=("Arial",12), bg="#6C13E7", width=11).place(x=5 , y= 300)


    DevelopmentTeam=PhotoImage(file="team.png")
    esqui2=Radiobutton(ScrumP,image=DevelopmentTeam,bg="#6C13E7").place(x=400 , y= 90)
    texto=Label(ScrumP, text="Development team", font=("Arial",12), bg="#E0E2EE").place(x=240 , y= 100)



    ProductOwner=PhotoImage(file="product.png")
    esqui2=Radiobutton(ScrumP,image=ProductOwner,bg="#6C13E7").place(x=620 , y= 90)
    texto=Label(ScrumP, text="Product Owner", font=("Arial",12), bg="#E0E2EE").place(x=700 , y= 100)

    proyectos=PhotoImage(file="proyectos.png")
    julian=Button(ScrumP,image=proyectos).place(x=220 , y= 170)
   
    texto=Label(ScrumP, text="Proyectos Creados", font=("Arial",12), bg="#E0E2EE").place(x=280 , y= 430) 


    crear=PhotoImage(file="crear.png")
    julian4=Button(ScrumP,image=crear).place(x=600 , y= 170)
   
    texto=Label(ScrumP, text="Crear un Proyecto", font=("Arial",12), bg="#E0E2EE").place(x=660 , y= 430) 

    ScrumP.mainloop()


menu()