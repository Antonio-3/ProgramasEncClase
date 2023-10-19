import tkinter as tk

def calcular_promedio_edad():
    try:
        anos_nacimiento = entry_anos_nacimiento.get().split()
        anos_nacimiento = [int(ano) for ano in anos_nacimiento]
        edad_total = sum([2023 - ano for ano in anos_nacimiento])
        promedio = edad_total / len(anos_nacimiento)
        resultado.set(f"El promedio de edad de las personas es: {promedio:.2f} años")
    except ValueError:
        resultado.set("Por favor, ingrese años de nacimiento válidos separados por espacios.")


ventana = tk.Tk()
ventana.title("Promedio de Edad de N Personas")


label_anos_nacimiento = tk.Label(ventana, text="Ingrese los años de nacimiento separados por espacios:")
label_anos_nacimiento.pack()
entry_anos_nacimiento = tk.Entry(ventana)
entry_anos_nacimiento.pack()


btn_calcular = tk.Button(ventana, text="Calcular Promedio de Edad", command=calcular_promedio_edad)
btn_calcular.pack()


resultado = tk.StringVar()
resultado.set("")
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()


ventana.mainloop()