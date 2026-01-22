import tkinter as tk
import random

def change_color():
    # Generate random RGB values
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Convert RGB to hex color
    color = f'#{r:02x}{g:02x}{b:02x}'

    # Change window background
    root.configure(bg=color)
    label.config(text=f"RGB: ({r}, {g}, {b})", bg=color)

# Create main window
root = tk.Tk()
root.title("Random RGB Color")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Click the button", font=("Arial", 16))
label.pack(pady=40)

# Button
btn = tk.Button(root, text="Change Color", font=("Arial", 14),
                command=change_color)
btn.pack()

# Run GUI
root.mainloop()
