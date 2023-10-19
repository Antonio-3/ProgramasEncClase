import tkinter as tk

def contar_aprobados():
    try:
        calificaciones = entry_calificaciones.get().split()
        calificaciones = [float(calificacion) for calificacion in calificaciones]
        aprobados = sum(1 for calificacion in calificaciones if calificacion >= 7)
        resultado.set(f"{aprobados} alumnos han aprobado la materia.")
    except ValueError:
        resultado.set("Por favor, ingrese calificaciones válidas separadas por espacios.")


ventana = tk.Tk()
ventana.title("Contar Alumnos Aprobados")


label_calificaciones = tk.Label(ventana, text="Ingrese las calificaciones de los alumnos (separadas por espacios):")
label_calificaciones.pack()
entry_calificaciones = tk.Entry(ventana)
entry_calificaciones.pack()


btn_contar = tk.Button(ventana, text="Contar Aprobados", command=contar_aprobados)
btn_contar.pack()


resultado = tk.StringVar()
resultado.set("")
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()


ventana.mainloop()