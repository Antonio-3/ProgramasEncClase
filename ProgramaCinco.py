import tkinter as tk

def calcular_edad():
    try:
        año_nacimiento = int(entry_año_nacimiento.get())
        año_actual = 2023
        edad = año_actual - año_nacimiento
        años_a_cumplir = edad + 1
        resultado.set(f"El próximo año cumplirás {años_a_cumplir} años.")
    except ValueError:
        resultado.set("Por favor, ingrese un año de nacimiento válido.")


ventana = tk.Tk()
ventana.title("Calcular Edad el Siguiente Año")
ventana.geometry("250x250")

label_año_nacimiento = tk.Label(ventana, text="Ingrese el año de nacimiento:")
label_año_nacimiento.pack()
entry_año_nacimiento = tk.Entry(ventana)
entry_año_nacimiento.pack()


btn_calcular = tk.Button(ventana, text="Calcular Edad", command=calcular_edad)
btn_calcular.pack()


resultado = tk.StringVar()
resultado.set("")
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()


ventana.mainloop()