# -Calculadoras-
Proyecto de calculadoras que intenta recrear la capacidad real para hacer cálculos simples e intermedios usando los fundamentos basicos de Python y la libreria de Tkinter. El proyecto se divide en tres fases:
1- Armado de una calculadora simple que pueda lograr los calculos idoneos como la suma, resta, multiplicacion y division (Tomando como referencia un ejemplo echo anteriormente de base).
2-Armado de una calculadora avanzada, capaz de hacer calculos de manera compleja aunque no sea perfecta. Aplicacndo un GUI atractivo para que sea mas comodo.



'import tkinter as tk': importa el modulo tkinter y lo renombra como 'tk'

'from tkinter import messagebox': importa la clase 'messagebox' del modulo 'tkinter'

'class Calculator(tk.Tk):' define una nueva clase llamada 'Calculator' que hereda de la clase 'tk.Tk'.
Esta clase representa la aplicacion principal de la calculadora.

'def __init__(self)': define el metodo de inicializacion de la clase. Este metodo se llama cuando se
crea una nueva instancia de la clase.

    'super().__init()': llamada al metodo de inicializacion de la clase base 



Un ejemplo de calculadora, con las propiedades de multiplicacion, suma, division, resta, la integracion de obtener un resultado
y el manejo de los decimales. Pero sin la posibilidad de usarla mas de una vez.


import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.result_var = tk.StringVar()

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
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Error en la expresión: {e}")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + value)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()


------------------------------------------------------------------------------------------------

Aqui la calculadora puede hacer todas las funcionalidades anteriores pero ahora se integro la posibilidad de usar las fracciones, las raizes y los exponentes.
Ademas de hacer calculos un poco mas complejos, pero simples. Tambien ahora es capaz de hacer distintas cuentas, ya que se pueden borrar los resultados y 
empezar un nuevo calculo.


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


-----------------------------------------------------------------------------------------------


Resultado final del proyecto, una calculadora que puede hacer calculos de maera simple pero eficaz, con una interfaz grafica de calculadora usando
la biblioteca Tkinter.




import tkinter as tk
from tkinter import messagebox

class AdvancedCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x600")
        self.configure(bg="#202020")
        self.result_var = tk.StringVar()
        self._create_widgets()

    def _create_widgets(self):
        # Pantalla
        display_frame = tk.Frame(self, bg="#202020")
        display_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        entry = tk.Entry(display_frame, textvariable=self.result_var, font=("Arial", 30), 
                         bg="#2d2d2d", fg="white", justify="right", relief="flat")
        entry.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=20)

        # Botones
        button_frame = tk.Frame(self, bg="#202020")
        button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        buttons = [
            ["%", "CE", "C", "\u232B"],
            ["1/x", "x²", "√", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ".", "="]
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = tk.Button(button_frame, text=text, font=("Arial", 18), 
                                bg="#333333" if r > 1 else "#505050", fg="white",
                                command=lambda t=text: self.on_button_click(t))
                btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

        # Configuración adaptable de las columnas y filas
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)
        for i in range(len(buttons)):
            button_frame.rowconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Error en la expresión: {e}")
        elif value == "C":
            self.result_var.set("")
        elif value == "\u232B":  # Retroceso
            self.result_var.set(self.result_var.get()[:-1])
        elif value == "CE":
            self.result_var.set("")
        elif value == "+/-":
            current = self.result_var.get()
            if current:
                if current[0] == "-":
                    self.result_var.set(current[1:])
                else:
                    self.result_var.set("-" + current)
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + value)

if __name__ == "__main__":
    app = AdvancedCalculator()
    app.mainloop()








