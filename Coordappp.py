import tkinter as tk
from tkinter import ttk
from pyproj import Proj, transform

# Define projection systems
wgs84 = Proj(init='epsg:4326')  # WGS 84
ghana_nat_grid = Proj(init='epsg:2136')  # Ghana National Grid
ghana_meter_grid = Proj(init='epsg:25000')  # Example EPSG code for Ghana Meter Grid


class CoordinateTransformationApp:
    def __init__(self, root):  # Corrected method name
        self.root = root
        self.root.title("Coordinate Transformation App")
        
        # Apply dark theme styles
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use a base theme to customize
        self.root.configure(bg='#2E2E2E')  # Dark background for the root window
        
        # Set dark theme for ttk widgets
        self.style.configure('TLabel', background='#2E2E2E', foreground='white')
        self.style.configure('TEntry', fieldbackground='#4D4D4D', foreground='white')
        self.style.configure('TButton', background='#3A3A3A', foreground='white')
        self.style.configure('TCombobox', fieldbackground='#4D4D4D', background='#2E2E2E', foreground='white')
        
        # Set up the user interface
        self.setup_ui()

    def setup_ui(self):
        # Input fields for coordinates
        self.input_label = ttk.Label(self.root, text="Input Coordinates:")
        self.input_label.grid(column=0, row=0, padx=10, pady=5)

        self.input_x_label = ttk.Label(self.root, text="X (Longitude):")
        self.input_x_label.grid(column=1, row=0, padx=10, pady=5)
        self.input_x = ttk.Entry(self.root)
        self.input_x.grid(column=2, row=0, padx=10, pady=5)

        self.input_y_label = ttk.Label(self.root, text="Y (Latitude):")
        self.input_y_label.grid(column=1, row=1, padx=10, pady=5)
        self.input_y = ttk.Entry(self.root)
        self.input_y.grid(column=2, row=1, padx=10, pady=5)

        # Dropdown for selecting transformation
        self.transformation_label = ttk.Label(self.root, text="Select Transformation:")
        self.transformation_label.grid(column=0, row=2, padx=10, pady=5)

        self.transformation = ttk.Combobox(self.root, values=[
            "WGS 84 to Ghana National Grid",
            "WGS 84 to Ghana Meter Grid",
            "Ghana National Grid to WGS 84",
            "Ghana Meter Grid to WGS 84"
        ])
        self.transformation.grid(column=1, row=2, padx=10, pady=5)

        # Button to perform transformation
        self.transform_button = ttk.Button(self.root, text="Transform", command=self.transform_coordinates)
        self.transform_button.grid(column=2, row=2, padx=10, pady=5)

        # Output fields for transformed coordinates
        self.output_label = ttk.Label(self.root, text="Output Coordinates:")
        self.output_label.grid(column=0, row=3, padx=10, pady=5)

        self.output_x_label = ttk.Label(self.root, text="X:")
        self.output_x_label.grid(column=1, row=3, padx=10, pady=5)
        self.output_x = ttk.Entry(self.root)
        self.output_x.grid(column=2, row=3, padx=10, pady=5)

        self.output_y_label = ttk.Label(self.root, text="Y:")
        self.output_y_label.grid(column=1, row=4, padx=10, pady=5)
        self.output_y = ttk.Entry(self.root)
        self.output_y.grid(column=2, row=4, padx=10, pady=5)

    def transform_coordinates(self):
        try:
            x = float(self.input_x.get())
            y = float(self.input_y.get())

            transformation_type = self.transformation.get()
            if transformation_type == "WGS 84 to Ghana National Grid":
                x2, y2 = transform(wgs84, ghana_nat_grid, x, y)
            elif transformation_type == "WGS 84 to Ghana Meter Grid":
                x2, y2 = transform(wgs84, ghana_meter_grid, x, y)
            elif transformation_type == "Ghana National Grid to WGS 84":
                x2, y2 = transform(ghana_nat_grid, wgs84, x, y)
            elif transformation_type == "Ghana Meter Grid to WGS 84":
                x2, y2 = transform(ghana_meter_grid, wgs84, x, y)
            else:
                raise ValueError("Invalid transformation type selected")

            self.output_x.delete(0, tk.END)
            self.output_y.delete(0, tk.END)
            self.output_x.insert(0, str(x2))
            self.output_y.insert(0, str(y2))
        except Exception as e:
            self.output_x.delete(0, tk.END)
            self.output_y.delete(0, tk.END)
            self.output_x.insert(0, "Error")
            self.output_y.insert(0, str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinateTransformationApp(root)
    root.mainloop()
