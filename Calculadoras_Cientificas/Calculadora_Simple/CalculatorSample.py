import tkinter as tk
from tkinter import messagebox
from fractions import Fraction

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Avanzada")
        self.geometry("400x500")
        self.result_var = tk.StringVar()
        self.memory = 0  # Variable para manejar memoria

        self.create_widgets()

    def create_widgets(self):
        # Pantalla
        entry_frame = tk.Frame(self)
        entry_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        entry = tk.Entry(entry_frame, textvariable=self.result_var, font=("Arial", 20), justify="right")
        entry.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Botones
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        buttons = [
            ("7", 1, 1), ("8", 1, 2), ("9", 1, 3), ("/", 1, 4),
            ("4", 2, 1), ("5", 2, 2), ("6", 2, 3), ("*", 2, 4),
            ("1", 3, 1), ("2", 3, 2), ("3", 3, 3), ("-", 3, 4),
            ("0", 4, 1), (".", 4, 2), ("=", 4, 3), ("+", 4, 4),
            ("C", 5, 1), ("%", 5, 2), ("M+", 5, 3), ("MR", 5, 4),
            ("√", 6, 1), ("x^y", 6, 2), ("1/x", 6, 3), ("MC", 6, 4),
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(button_frame, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew")

        # Configurar la distribución de las columnas y filas
        for i in range(1, 5):
            button_frame.columnconfigure(i, weight=1)
            button_frame.rowconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == "=":
            self.calculate_result()
        elif value == "C":
            self.result_var.set("")
        elif value == "M+":
            try:
                self.memory += float(self.result_var.get())
                self.result_var.set("")
            except ValueError:
                messagebox.showerror("Error", "No se puede agregar a memoria.")
        elif value == "MR":
            self.result_var.set(str(self.memory))
        elif value == "MC":
            self.memory = 0
        elif value == "%":
            try:
                result = float(self.result_var.get()) / 100
                self.result_var.set(result)
            except ValueError:
                messagebox.showerror("Error", "Porcentaje inválido.")
        elif value == "√":
            try:
                result = float(self.result_var.get()) ** 0.5
                self.result_var.set(result)
            except ValueError:
                messagebox.showerror("Error", "Raíz cuadrada inválida.")
        elif value == "1/x":
            try:
                result = 1 / float(self.result_var.get())
                self.result_var.set(result)
            except ZeroDivisionError:
                messagebox.showerror("Error", "División por cero.")
            except ValueError:
                messagebox.showerror("Error", "Operación inválida.")
        elif value == "x^y":
            current_text = self.result_var.get() + "**"
            self.result_var.set(current_text)
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + value)

    def calculate_result(self):
        try:
            # Evaluar de manera segura
            expression = self.result_var.get()
            result = eval(expression)
            self.result_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", f"Error en la expresión: {e}")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
