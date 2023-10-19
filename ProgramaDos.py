import tkinter as tk


ventana = tk.Tk()
ventana.title("Venta de Productos")
ventana.geometry("250x250")


productos = ["Torta", "Tacos", "Hotdog", "Pizza"]
precios = [5.0, 3.0, 2.5, 7.0]
seleccion = []


def calcular_total():
    total = sum(cantidad.get() * precio for cantidad, precio in zip(seleccion, precios))
    label_total.config(text=f"Total: ${total:.2f}")


for i, producto in enumerate(productos):
    label = tk.Label(ventana, text=producto)
    label.grid(row=i, column=0)

    cantidad = tk.IntVar()
    entry = tk.Entry(ventana, textvariable=cantidad)
    entry.grid(row=i, column=1)
    seleccion.append(cantidad)


btn_calcular = tk.Button(ventana, text="Calcular Total", command=calcular_total)
btn_calcular.grid(row=len(productos), column=0, columnspan=2)


label_total = tk.Label(ventana, text="Total: $0.00")
label_total.grid(row=len(productos) + 1, column=0, columnspan=2)


ventana.mainloop()