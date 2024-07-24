import tkinter as tk
from math import pi, tan

def calculate_area():
    try:
        n = int(sides_entry.get())
        s = float(side_length_entry.get())
        if n < 3:
            result_label.config(text="Number of sides must be >= 3")
            return
        area = (n * s**2) / (4 * tan(pi / n))
        result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")


root = tk.Tk()
root.title("N-Sided Polygon Area Calculator")
root.configure(bg="aqua")
root.geometry("250x250")


tk.Label(root, text="Number of sides:").pack(pady=5)
sides_entry = tk.Entry(root)
sides_entry.pack(pady=5)

tk.Label(root, text="Length of each side:").pack(pady=5)
side_length_entry = tk.Entry(root)
side_length_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Area: ")
result_label.pack(pady=10)

# Running the application
root.mainloop()
