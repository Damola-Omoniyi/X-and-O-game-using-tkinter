import tkinter as tk
from tkinter import ttk
import asyncio
import websockets
import json

async def send_command(command):
    uri = "ws://192.168.234.21:8765"  # Replace with Pico’s IP
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"command": command}))
        print(f"Sent: {command}")

# Initialize the main window
root = tk.Tk()
root.title("CAR GUI")

# Set the size of the window
root.geometry("400x300")

# Create a frame to hold the widgets
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create entry boxes and labels
move_var = tk.StringVar()
speed_var = tk.StringVar()

move_label = ttk.Label(frame, text="Move:", font=("Arial", 14))
move_label.grid(row=0, column=0, padx=10, pady=10)
move_entry = ttk.Entry(frame, textvariable=move_var, font=("Arial", 14))
move_entry.grid(row=0, column=1, padx=10, pady=10)

speed_label = ttk.Label(frame, text="Speed:", font=("Arial", 14))
speed_label.grid(row=1, column=0, padx=10, pady=10)
speed_entry = ttk.Entry(frame, textvariable=speed_var, font=("Arial", 14))
speed_entry.grid(row=1, column=1, padx=10, pady=10)

# Define the action to be performed when the button is pressed
def action():
    move = move_var.get()
    speed = int(speed_var.get())
    print(f"Move: {move}, Speed: {speed}")
    commands = [move, speed]
    asyncio.run(send_command(commands))  # Pico should move left

# Add the action button
action_button = ttk.Button(frame, text="Submit", command=action, style="TButton", padding=10)
action_button.grid(row=2, column=0, columnspan=2, pady=20)

# Start the main event loop
root.mainloop()
