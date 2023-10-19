import tkinter as tk

def calcular_cuadrado():
    try:
        numero = float(entry_numero.get())
        if numero >= 0:
            resultado.set(f"El cuadrado de {numero} es: {numero**2:.2f}")
        else:
            resultado.set("Por favor, ingrese un número positivo.")
    except ValueError:
        resultado.set("Por favor, ingrese un número válido.")


ventana = tk.Tk()
ventana.title("Calcular Cuadrado de un Número")


label_numero = tk.Label(ventana, text="Ingrese un número positivo:")
label_numero.pack()
entry_numero = tk.Entry(ventana)
entry_numero.pack()


btn_calcular = tk.Button(ventana, text="Calcular Cuadrado", command=calcular_cuadrado)
btn_calcular.pack()


resultado = tk.StringVar()
resultado.set("")
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()


ventana.mainloop()