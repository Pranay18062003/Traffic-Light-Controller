# Traffic Light Controller (Beginner Visual Version)
# Made by Pranay Anand 💡

import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Traffic Light Controller 🚦")
root.geometry("250x400")
root.config(bg="black")

# Create a canvas to draw the traffic light
canvas = tk.Canvas(root, width=200, height=350, bg="black", highlightthickness=0)
canvas.pack(pady=20)

# Draw the traffic light outline
canvas.create_rectangle(50, 50, 150, 300, outline="white", width=3)

# Draw circles for red, yellow, and green lights
red = canvas.create_oval(70, 60, 130, 120, fill="gray")
yellow = canvas.create_oval(70, 140, 130, 200, fill="gray")
green = canvas.create_oval(70, 220, 130, 280, fill="gray")

# Text label to show status (STOP / WAIT / GO)
status_label = tk.Label(root, text="Starting...", font=("Arial", 14, "bold"), bg="black", fg="white")
status_label.pack(pady=10)

# Function to change lights
def traffic_lights():
    while True:
        # RED Light
        canvas.itemconfig(red, fill="red")
        canvas.itemconfig(yellow, fill="gray")
        canvas.itemconfig(green, fill="gray")
        status_label.config(text="STOP 🚫", fg="red")
        root.update()
        time.sleep(3)

        # GREEN Light
        canvas.itemconfig(red, fill="gray")
        canvas.itemconfig(yellow, fill="gray")
        canvas.itemconfig(green, fill="green")
        status_label.config(text="GO ✅", fg="green")
        root.update()
        time.sleep(3)

        # YELLOW Light
        canvas.itemconfig(red, fill="gray")
        canvas.itemconfig(yellow, fill="yellow")
        canvas.itemconfig(green, fill="gray")
        status_label.config(text="WAIT ⚠️", fg="yellow")
        root.update()
        time.sleep(2)

# Run the traffic light after 1 second
root.after(1000, traffic_lights)

# Keep the window running
root.mainloop()
