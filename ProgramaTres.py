import tkinter as tk

def determinar_dia():
    try:
        numero = int(entry_numero.get())
        if 1 <= numero <= 7:
            dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
            resultado.set(f"El número {numero} corresponde a {dias[numero - 1]}.")
        else:
            resultado.set("Número fuera del rango (1-7).")
    except ValueError:
        resultado.set("Por favor, ingrese un número válido.")


ventana = tk.Tk()
ventana.title("Determinar Día de la Semana")
ventana.geometry("250x250")


label_numero = tk.Label(ventana, text="Ingrese un número (1-7):")
label_numero.pack()
entry_numero = tk.Entry(ventana)
entry_numero.pack()


btn_determinar = tk.Button(ventana, text="Determinar Día", command=determinar_dia)
btn_determinar.pack()


resultado = tk.StringVar()
resultado.set("")
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()


ventana.mainloop()