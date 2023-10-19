import tkinter as tk

def calcular_promedio():
    try:
        numeros = entry_numeros.get().split()
        numeros = [float(numero) for numero in numeros if float(numero) > 0]
        if len(numeros) > 0:
            promedio = sum(numeros) / len(numeros)
            resultado.set(f"El promedio de los números positivos es: {promedio:.2f}")
        else:
            resultado.set("No se ingresaron números positivos.")
    except ValueError:
        resultado.set("Por favor, ingrese números válidos separados por espacios.")


ventana = tk.Tk()
ventana.title("Promedio de N Números Positivos")


label_numeros = tk.Label(ventana, text="Ingrese N números positivos separados por espacios:")
label_numeros.pack()
entry_numeros = tk.Entry(ventana)
entry_numeros.pack()


btn_calcular = tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio)
btn_calcular.pack()


resultado = tk.StringVar()
resultado.set("")
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()


ventana.mainloop()