from tkinter import *


def menu():
    ScrumP=Tk()
    ScrumP.title("Scrum Alliance")
    ScrumP.geometry("980x550")
    ScrumP.config(bg="#E0E2EE")

    morado=Frame(ScrumP)
    morado.pack(anchor="n")
    morado.config(bg="#6C13E7", width=980,height=85)
   #logos redes sociales 
    instagram=PhotoImage(file="instagram.png")
    julian=Button(ScrumP,image=instagram,bg="#6C13E7",bd=0).place(x=720 , y= 20)

    facebook=PhotoImage(file="facebook.png")
    julian2=Button(ScrumP,image=facebook,bg="#6C13E7",bd=0).place(x=790 , y= 20)

    whatsapp=PhotoImage(file="whatsapp.png")
    julian3=Button(ScrumP,image=whatsapp,bg="#6C13E7",bd=0).place(x=860 , y= 20)

    #imagenes
    imagen=PhotoImage(file="Scrum.png")
    esqui=Label(ScrumP,image=imagen).place(x=30 , y= 170)

    imagen1=PhotoImage(file="Logo.png")
    esqui1=Label(ScrumP,image=imagen1).place(x=10 , y= 15)
   
    texto=Label(ScrumP, text="Bienvenido a Scrum Alliance\n\n¡¡Insistir, persistir y no desistir!!", font=("Arial",12), bg="#E0E2EE").place(x=120 , y= 360) 

    #Cuadro Login
    azul=Frame(ScrumP)
    azul.pack()
    azul.config(bg="#6C13E7", width=280,height=280)
    azul.place (x=580 , y=170)



    # Cuadro Login y Register
    hola=Label(ScrumP, text="Ingrese el usuario registrado\n o registrese:", font=("Arial",12), bg="#6C13E7").place(x=610 , y= 175) 
    

    hola1=Label(ScrumP, text="Ingrese el usuario:", font=("Arial",12), bg="#6C13E7").place(x=610 , y= 230)
    cuadro=Entry(ScrumP, font=("Arial",12), bg="#FFFFFF").place(x=610 , y= 260)
    

    hola2=Label(ScrumP, text="Ingrese la clave:", font=("Arial",12), bg="#6C13E7").place(x=610 , y= 300)
    cuadro1=Entry(ScrumP, font=("Arial",12), bg="#FFFFFF",show="*").place(x=610 , y= 330)

    boton=Button(ScrumP, text="Entrar", font=("Arial",12), bg="#E0E2EE", width=5).place(x=610 , y= 380)

    boton=Button(ScrumP, text="Registrarse", font=("Arial",12), bg="#E0E2EE", width=9).place(x=700 , y= 380)

    ScrumP.mainloop()


menu()


