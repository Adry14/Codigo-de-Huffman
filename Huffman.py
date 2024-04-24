import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

#explicaciones del programa
#esta es la funcion para buscar el archivo en la pc 
def examinar_archivo():
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, 'r') as file:
            contenido = file.read()
            texto.config(state=tk.NORMAL)
            texto.delete('1.0', tk.END)
            texto.insert(tk.END, contenido)
            texto.config(state=tk.DISABLED)
            calcular_frecuencia(contenido)
#esta funcion calcula la veces que se repiten las letras dentro del archivo que se subio
def calcular_frecuencia(contenido):
    frecuencias = {}
    for letra in contenido:
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    with open("frecuencias.txt", 'w') as file:
        for letra, frecuencia in frecuencias.items():
            file.write(f"{letra}: {frecuencia}\n")
    frecuencias_texto.config(state=tk.NORMAL)
    frecuencias_texto.delete('1.0', tk.END)
    for letra, frecuencia in frecuencias.items():
        frecuencias_texto.insert(tk.END, f"{letra}: {frecuencia}\n")
    frecuencias_texto.config(state=tk.DISABLED)

#empezamos con la farte grafica
#esta es para inicar nuestra ventana
ventana = tk.Tk()
ventana.title("Programa")
ventana.geometry("800x600") #tamaño de la ventana

etiqueta= tk.Label(ventana, text="Bienvenido", bg="light blue", font="Arial 20") #texto de bienvenida
etiqueta.pack(fill=tk.X)

boton_examinar = tk.Button(ventana, text="Examinar:", command=examinar_archivo, bg="light green", font="arial 10") #tenemos el primer boton que es el de eexaminar que la hacer click se abre el buscador para subir el archivo
boton_examinar.pack(pady=10)

texto = tk.Text(ventana, height=10, width=50) #esta es el recuadro de texto vacio, aqui en principo aparacera la frase que viene en el archivo que se subia
texto.pack()                                  #ademas de que mostrara el las letras y el numero de veces que se repitio cada una

frecuencias_texto = tk.Text(ventana, height=10, width=50)#este es el segundo cuadro de texto vacio, aqui en principo es el apartado en donde se imprimira el texto(donde se realiza los algortimos)
frecuencias_texto.pack()                                #aqui es donde aparecera la respuesta cuando le das click a la opcion de comprimir o descomprimir. asi que aqui deberas de enlazar tu programa y se mostrara el resultado

#estos son los botones de las funciones del programa donde pues deberas enlazar a cada boton su funcion al momento de hacer click en uno de ellos
#ademas de su funcion, tienes el cuadro de texto arriba donde se vera reflejado segun el boton que diste click
boton_comprimir = tk.Button(ventana, text="Comprimir Cadena: ",bg="orange", font="arial 10")
boton_comprimir.pack(padx=60, pady=10)

boton_comprimir = tk.Button(ventana, text="Descomprimir Cadena: ",bg="orange", font="arial 10")
boton_comprimir.pack(padx=10, pady=10)

#main para la ventana
ventana.mainloop()
