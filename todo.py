
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
    esqui1=Label(ScrumP,image=imagen1).place(x=10 , y= 15)

    def destry1():
        ScrumP.destroy()
 
    back=PhotoImage(file="back.png")
    cote3=Button(ScrumP,image=back,bg="#6C13E7",bd=0,command=destry1).place(x=890 , y= 20)


    boton1=Button(ScrumP, text="ScrumBoard", font=("Arial",12), bg="#6C13E7", width=11).place(x=5 , y= 180)
    boton2=Button(ScrumP, text="To Do", font=("Arial",12), bg="#6C13E7", width=11).place(x=5 , y= 220)
    boton3=Button(ScrumP, text="In Progress", font=("Arial",12), bg="#6C13E7", width=11).place(x=5 , y= 260)
    boton4=Button(ScrumP, text="Done", font=("Arial",12), bg="#6C13E7", width=11).place(x=5 , y= 300)

    azul=Frame(ScrumP)
    azul.pack()
    azul.config(bg="#6C13E7", width=180,height=70)
    azul.place (x=500 , y=130)
    texto=Label(ScrumP, text="To Do", font=("Arial",30), bg="#6C13E7").place(x=530 , y= 140)

   #Agregar tareas
    hola1=Label(ScrumP, text="Agregrar Tareas\n Numero de tareas:", font=("Arial",12), bg="#6C13E7",width="21").place(x=180 , y= 230)
    cuadro=Entry(ScrumP, font=("Arial",12), bg="#FFFFFF",width="10").place(x=230 , y= 280)
    boton=Button(ScrumP, text="Agregar",font=("Arial",12),bg="#E0E2EE",width="9").place(x= 230, y= 310)
    hola1=Label(ScrumP, text="¡Tienes\n tareas por realizar!", font=("Arial",12), bg="#6C13E7",width="21").place(x=180 , y= 350)
    cuidado=PhotoImage(file="warning.png")
    esqui1=Label(ScrumP,image=cuidado).place(x=230 , y= 410)

    #Tareas por realizar
    hola1=Label(ScrumP, text="Tareas por\n Realizar:", font=("Arial",12), bg="#6C13E7",width="21").place(x=480 , y= 230)
    cuadro=Entry(ScrumP, font=("Arial",12), bg="#FFFFFF",width="10").place(x=530 , y= 280)
    boton=Button(ScrumP, text="Visualizar",font=("Arial",12),bg="#E0E2EE",width="9").place(x= 530, y= 310)
    hola1=Label(ScrumP, text="¡Tienes\n tareas por realizar!", font=("Arial",12), bg="#6C13E7",width="21").place(x=480 , y= 350)
    programador=PhotoImage(file="programadores.png")
    esqui1=Label(ScrumP,image=programador).place(x=490 , y= 410)

    #Ver tareas por realizar
    hola1=Label(ScrumP, text="Ver tareas\n Conjuntas:", font=("Arial",12), bg="#6C13E7",width="21").place(x=760 , y= 230)
    cuadro=Entry(ScrumP, font=("Arial",12), bg="#FFFFFF",width="10").place(x=810 , y= 280)
    boton=Button(ScrumP, text="Visualizar",font=("Arial",12),bg="#E0E2EE",width="9").place(x= 810, y= 310)
    hola1=Label(ScrumP, text="¡Tienes\n tareas por realizar!", font=("Arial",12), bg="#6C13E7",width="21").place(x=760 , y= 350)
    
    trabajo=PhotoImage(file="equipo.png")
    esqui2=Label(ScrumP,image=trabajo).place(x=790 , y= 410)

    #Boton Siguiente pagina
    siguiente=Frame(ScrumP)
    siguiente.pack(anchor="se")
    siguiente.config(bg="#6C13E7", width=180,height=70)
    texto=Button(ScrumP, text="In Progress", font=("Arial",16), bg="#6C13E7",bd=0).place(x=810 , y= 100)

    flecha=PhotoImage(file="flecha.png")
    esqui2=Button(ScrumP,image=flecha,bg="#6C13E7").place(x=928 , y= 100)

    ScrumP.mainloop()


menu()