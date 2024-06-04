#Uma calculadora simples que pode realizar operações básicas como adição, subtração, multiplicação e divisão.
import tkinter as tk
from tkinter import messagebox

#Funções de Operações
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y ==0:
        return "Erro ao dividir por 0"
    else:
        return x/y


# Função para calcular
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == '1':
        result = add(num1, num2)
    elif operation == '2':
        result = subtract(num1, num2)
    elif operation == '3':
        result = multiply(num1, num2)
    elif operation == '4':
        result = divide(num1, num2)
    else:
        result = "Operação inválida"

    result_label.config(text=f'Resultado: {result}')

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora")

# Criar widgets
operation_var = tk.StringVar()

tk.Label(root, text="Selecione uma operação:").grid(row=0, column=0, columnspan=2)

tk.Radiobutton(root, text="Adição", variable=operation_var, value='1').grid(row=1, column=0, sticky='w')
tk.Radiobutton(root, text="Subtração", variable=operation_var, value='2').grid(row=1, column=1, sticky='w')
tk.Radiobutton(root, text="Multiplicação", variable=operation_var, value='3').grid(row=2, column=0, sticky='w')
tk.Radiobutton(root, text="Divisão", variable=operation_var, value='4').grid(row=2, column=1, sticky='w')

tk.Label(root, text="Digite o primeiro número:").grid(row=3, column=0, columnspan=2)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=4, column=0, columnspan=2)

tk.Label(root, text="Digite o segundo número:").grid(row=5, column=0, columnspan=2)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=6, column=0, columnspan=2)

tk.Button(root, text="Calcular", command=calculate).grid(row=7, column=0, columnspan=2)

result_label = tk.Label(root, text="Resultado: ")
result_label.grid(row=8, column=0, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()
        

