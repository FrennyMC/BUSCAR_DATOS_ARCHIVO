from tkinter import *
from tkinter import messagebox
from io import open
# Interfaz gráfica 

#Programa
"""Función Principal_ Lógica dentro del programa donde se implementan los margenes
y formatos para la vistad de la interfaz del programa principal"""
def main():
    # Vista Ventana Principal
    ventana = Tk()
    ventana.title("")
    ventana.geometry("400x500")
    ventana.config(bg= "blue")
    etiqueta_1 = Label(ventana, text = "TICO SEGURO COVID", font=("Tahoma",10), bg= "black", fg="white",width = "100",height= "3")
    etiqueta_1.pack()
    etiqueta = Label(ventana, text = BuscarDato("persona.txt"), font=("Tahoma",12), bg= "blue", fg="white",width = "100",height= "1")
    etiqueta.pack()



    #Insertar Imágenes Pantalla Principal 
    logo = PhotoImage(file = "Zona_Blanca.gif")
 
    # Margenes posiciones en tkinter
    fondo = Label(ventana, image = logo, height = 330, width = 340).place(x=30, y=150)

    # ID's
    code_pass_1 = PhotoImage(file = BuscarDato("cedula.txt"))
    code_pass_2 = PhotoImage(file = BuscarDato("vacunas.txt"))
    code_pass_3 = PhotoImage(file = BuscarDato("examen.txt"))
        
    #Funciones para los botones 
    def pass_1():
        pase_1 = Label(ventana, image= code_pass_1)
        pase_1.place(x= 50, y= 200)
         
    def pass_2():
        pase_2 = Label(ventana, image= code_pass_2)
        pase_2.place(x= 50, y= 200)

    def pass_3():
        pase_3 = Label(ventana, image= code_pass_3)
        pase_3.place(x= 50, y= 200)
        
    def pass_4():
        pase_4 = Label(ventana, image= code_pass_4)
        pase_4.place(x= 50, y= 200)

    #Botones Seleccionar
    botComp_1 = Button(ventana, text= "Foto ID", command= pass_1, bg= "#3366FF")
    botComp_1.place(x = 25, y= 100)
    botComp_1.config(fg= "white")


    botComp_2 = Button(ventana, text= "Vacunas", command= pass_2, bg= "#3366FF")
    botComp_2.place(x = 125, y= 100)
    botComp_2.config(fg= "white")

    botComp_3 = Button(ventana, text= "Prueba PCR", command= pass_3, bg= "#3366FF")
    botComp_3.place(x = 250, y= 100)
    botComp_3.config(fg= "white")

    etiqueta.mainloop()




"""Función que se encarga de buscar datos dentro de los archivos"""

def BuscarDato(Nombre_Archivo):
    try:
        with open(Nombre_Archivo, encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for i in lineas:
                ruta = i.strip()  # ¡Muy importante!
            if len(ruta) > 200:
                raise Exception("Límite de símbolos sobrepasado.")
            return ruta
    except FileNotFoundError as e:
        print("No Definido:", e)
        return "NO_ENCONTRADO.gif"  # Asegúrate de tener esta imagen o maneja el error


main()


