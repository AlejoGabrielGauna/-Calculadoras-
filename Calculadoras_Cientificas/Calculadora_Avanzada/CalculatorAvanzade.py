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
