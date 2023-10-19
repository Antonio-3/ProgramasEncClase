import tkinter as tk

def calcular_suma():
    numeros = []
    for entry in entradas:
        try:
            numero = float(entry.get())
            if 5 <= numero <= 10:
                numeros.append(numero)
            else:
                resultado.set("Los números deben estar en el rango de 5 a 10.")
                return
        except ValueError:
            resultado.set("Por favor, ingrese números válidos.")
            return

    if len(numeros) == 5:
        suma = sum(numeros)
        resultado.set(f"La suma de los números es: {suma}")
    else:
        resultado.set("Debe ingresar exactamente 5 números en el rango de 5 a 10.")


ventana = tk.Tk()
ventana.title("Suma de Números entre 5 y 10")
ventana.geometry("250x250")


entradas = []
for i in range(5):
    label = tk.Label(ventana, text=f"Ingrese el número {i + 1}:")
    label.pack()
    entrada = tk.Entry(ventana)
    entrada.pack()
    entradas.append(entrada)


btn_calcular = tk.Button(ventana, text="Calcular Suma", command=calcular_suma)
btn_calcular.pack()


resultado = tk.StringVar()
resultado.set("")
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()


ventana.mainloop()