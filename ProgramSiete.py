import tkinter as tk

def calcular_suma_cuadrados():
    try:
        numeros = entry_numeros.get().split()
        numeros = [int(numero) for numero in numeros if numero.isdigit()]
        suma = sum([n**2 for n in numeros])
        resultado.set(f"La suma de los cuadrados es: {suma}")
    except ValueError:
        resultado.set("Por favor, ingrese números válidos.")


ventana = tk.Tk()
ventana.title("Suma de Cuadrados de N Números")
ventana.geometry("250x250")

label_numeros = tk.Label(ventana, text="Ingrese N números separados por espacios:")
label_numeros.pack()
entry_numeros = tk.Entry(ventana)
entry_numeros.pack()


btn_calcular = tk.Button(ventana, text="Calcular Suma de Cuadrados", command=calcular_suma_cuadrados)
btn_calcular.pack()


resultado = tk.StringVar()
resultado.set("")
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()


ventana.mainloop()