
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

    ScrumP.config(bg="#E0E2EE")
    morado=Frame(ScrumP)
    morado.pack(anchor="center")
    morado.config(bg="#6C13E7", width=190,height=60)
    texto=Label(ScrumP, text="ScrumBoard", font=("Arial",20), bg="#6C13E7").place(x=470 , y= 100)



    imagen1=PhotoImage(file="Logo.png")
    esqui1=Label(ScrumP,image=imagen1).place(x=10 , y= 15)

    def destry1():
        ScrumP.destroy()
 
    back=PhotoImage(file="back.png")
    cote3=Button(ScrumP,image=back,bg="#6C13E7",bd=0,command=destry1).place(x=890 , y= 20)


    boton1=Button(ScrumP, text="ScrumBoard", font=("Arial",12), bg="#6C13E7", width=11).place(x=5 , y= 180)
    boton2=Button(ScrumP, text="To Do", font=("Arial",12), bg="#6C13E7", width=11).place(x=5 , y= 220)
    boton3=Button(ScrumP, text="In Progress", font=("Arial",12), bg="#6C13E7", width=11).place(x=5 , y= 260)
    boton4=Button(ScrumP, text="Done", font=("Arial",12), bg="#6C13E7", width=11).place(x=5 , y= 300)

    #Imagenes To do, In progress, Done

    todo=PhotoImage(file="todo.png")
    cote=Button(ScrumP,image=todo).place(x=175 , y= 170)
    texto=Label(ScrumP, text="To Do", font=("Arial",12), bg="#E0E2EE").place(x=255 , y= 390)


    inprogress=PhotoImage(file="progress.png")
    cote1=Button(ScrumP,image=inprogress).place(x=420 , y= 170)
    texto=Label(ScrumP, text="In\n Progress", font=("Arial",12), bg="#E0E2EE").place(x=480 , y= 390)


    done=PhotoImage(file="done.png")
    cote2=Button(ScrumP,image=done).place(x=670 , y= 170)
    texto=Label(ScrumP, text="Done", font=("Arial",12), bg="#E0E2EE").place(x=750 , y= 390)

    ScrumP.mainloop()


menu()