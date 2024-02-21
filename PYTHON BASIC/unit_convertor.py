import tkinter as tk
from tkinter import ttk

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Unit Converter')

        self.conversion_factors = {
            'Length': {'Centimeter': 1, 'Meter': 0.01, 'Km': 0.00001, 'Inch': 0.393701, 'Mile': 6.2137e-6,'foot': 0.0328084, 'square-feet': 0.00107639, 'Acre': 0.000247105, 'Square-Meters': 0.0001},
            'Mass': {'Micrograms': 1e6, 'Milligram': 1000, 'Gram': 1, 'Kilogram': 0.001, 'Tonne': 1e-6, 'Pound': 0.00220462},
            'Temperature': {'Kelvin': 1, 'Celsius': 273.15, 'Fahrenheit': 459.67},
            'Time': {'Second': 1, 'Minute': 1/60, 'Hour': 1/3600, 'Day': 1/86400},
            'Speed': {'Meters per second': 1, 'Kilometers per hour': 3.6, 'Mile per hour': 2.23694},
            'Energy': {'Joule': 1, 'Kilojoule': 0.001, 'Kilocalorie': 0.000239006},
            'Pressure': {'Bar': 1e-5, 'Pascal': 100000, 'Standard atmosphere': 0.000986923}
        }

        # Dropdowns
        self.unit_type_var = tk.StringVar()
        self.unit_from_var = tk.StringVar()
        self.unit_to_var = tk.StringVar()

        self.unit_type_label = ttk.Label(root, text='Select Conversion Type:')
        self.unit_type_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.unit_type_dropdown = ttk.Combobox(root, textvariable=self.unit_type_var, values=list(self.conversion_factors.keys()))
        self.unit_type_dropdown.grid(row=0, column=1, padx=10, pady=10)

        self.unit_from_label = ttk.Label(root, text='From:')
        self.unit_from_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.unit_from_dropdown = ttk.Combobox(root, textvariable=self.unit_from_var, values=[])
        self.unit_from_dropdown.grid(row=1, column=1, padx=10, pady=10)

        self.unit_to_label = ttk.Label(root, text='To:')
        self.unit_to_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.unit_to_dropdown = ttk.Combobox(root, textvariable=self.unit_to_var, values=[])
        self.unit_to_dropdown.grid(row=2, column=1, padx=10, pady=10)

        # Entry for value
        self.entry_label = ttk.Label(root, text='Value:')
        self.entry_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry = ttk.Entry(root)
        self.entry.grid(row=3, column=1, padx=10, pady=10)

        # Convert button
        self.convert_button = ttk.Button(root, text='Convert', command=self.convert)
        self.convert_button.grid(row=4, column=0,columnspan=10, padx=80, pady=10,sticky='nswe')

        # Result Label
        self.result_label = ttk.Label(root, text='')
        self.result_label.grid(row=6, columnspan=4, padx=10, pady=20)

        # Bind function to type selection change
        self.unit_type_var.trace_add('write', self.update_units_dropdown)

    def update_units_dropdown(self, *args):
        selected_type = self.unit_type_var.get()
        units = list(self.conversion_factors[selected_type].keys())

        self.unit_from_dropdown['values'] = units
        self.unit_to_dropdown['values'] = units

        # Set default values for dropdowns
        self.unit_from_var.set(units[0])
        self.unit_to_var.set(units[0])

    def convert(self):
        try:
            value = float(self.entry.get())
            unit_from = self.unit_from_var.get()
            unit_to = self.unit_to_var.get()
            unit_type = self.unit_type_var.get()

            if unit_from == unit_to:
                self.result_label.config(text='Same units. No conversion needed.')
            else:
                conversion_factor = self.conversion_factors[unit_type][unit_to] / self.conversion_factors[unit_type][unit_from]
                result_value = value * conversion_factor
                self.result_label.config(text=f'{value} {unit_from} is {result_value:.6f} {unit_to}')
        except ValueError:
            self.result_label.config(text='Invalid input. Please enter a valid number.')

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.geometry("380x280")
    root.title("UNIT CONVERSION")
    root.configure(bg="lightgrey")
    root.mainloop()
