import tkinter as tk

def calcular_suma():
    numeros = entry_numeros.get()
    numeros = numeros.split()  # Dividir los números ingresados en una lista
    suma_cuadrados_pares = 0
    suma_cubos_impares = 0

    for numero in numeros:
        try:
            n = int(numero)
            if n > 0:
                if n % 2 == 0:  # Par
                    suma_cuadrados_pares += n**2
                else:  # Impar
                    suma_cubos_impares += n**3
            else:
                resultado.set("Por favor, ingrese números positivos.")
                return
        except ValueError:
            resultado.set("Por favor, ingrese números válidos.")
            return

    resultado.set(f"La suma de los cuadrados de los pares es: {suma_cuadrados_pares}\n"
                  f"La suma de los cubos de los impares es: {suma_cubos_impares}")


ventana = tk.Tk()
ventana.title("Suma de Cuadrados y Cubos")
ventana.geometry("350x350")

label_numeros = tk.Label(ventana, text="Ingrese números positivos separados por espacios:")
label_numeros.pack()
entry_numeros = tk.Entry(ventana)
entry_numeros.pack()

btn_calcular = tk.Button(ventana, text="Calcular Suma", command=calcular_suma)
btn_calcular.pack()


resultado = tk.StringVar()
resultado.set("")
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()


ventana.mainloop()