'''

'import tkinter as tk': importa el modulo tkinter y lo renombra como 'tk'

'from tkinter import messagebox': importa la clase 'messagebox' del modulo 'tkinter'

'class Calculator(tk.Tk):' define una nueva clase llamada 'Calculator' que hereda de la clase 'tk.Tk'.
Esta clase representa la aplicacion principal de la calculadora.

'def __init__(self)': define el metodo de inicializacion de la clase. Este metodo se llama cuando se
crea una nueva instancia de la clase.

    'super().__init()': llamada al metodo de inicializacion de la clase base 


'''



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