import tkinter as tk

def sumar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado.set(num1 + num2)

def restar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado.set(num1 - num2)

def multiplicar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado.set(num1 * num2)

def dividir():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 != 0:
        resultado.set(num1 / num2)
    else:
        resultado.set("Error: División por cero")


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("250x250")


resultado = tk.StringVar()
resultado.set("Resultado")


label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack()
entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack()
entry_num2 = tk.Entry(ventana)
entry_num2.pack()


btn_sumar = tk.Button(ventana, text="Sumar", command=sumar)
btn_sumar.pack()
btn_restar = tk.Button(ventana, text="Restar", command=restar)
btn_restar.pack()
btn_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
btn_multiplicar.pack()
btn_dividir = tk.Button(ventana, text="Dividir", command=dividir)
btn_dividir.pack()


label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()


ventana.mainloop()