import tkinter as tk

def calcular_suma_cuadrados():
    suma_pares = 0
    suma_impares = 0

    for num in range(21):
        cuadrado = num**2
        if num % 2 == 0:
            suma_pares += cuadrado
        else:
            suma_impares += cuadrado

    resultado.set(f"La suma de los cuadrados de los números pares es: {suma_pares}\n"
                  f"La suma de los cuadrados de los números impares es: {suma_impares}")


ventana = tk.Tk()
ventana.title("Suma de Cuadrados de Números Pares e Impares")
ventana.geometry("500x125")


btn_calcular = tk.Button(ventana, text="Calcular Suma de Cuadrados", command=calcular_suma_cuadrados)
btn_calcular.pack()


resultado = tk.StringVar()
resultado.set("")
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()


ventana.mainloop()