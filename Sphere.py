import customtkinter as ctk

# Setup main window
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Voice Assistant Button")
app.geometry("400x300")

# Canvas for drawing the sphere
canvas = ctk.CTkCanvas(app, width=400, height=300, bg="#1e1e1e", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Draw sphere (as mic button)
x, y, r = 200, 150, 50
sphere = canvas.create_oval(x - r, y - r, x + r, y + r, fill="#00bfff", outline="")

# Animation logic
def animate_press():
    """Shrink and restore the sphere on click (press effect)."""
    for scale in [0.9, 1.0]:  # shrink then back to normal
        new_r = r * scale
        canvas.coords(sphere, x - new_r, y - new_r, x + new_r, y + new_r)
        app.update()
        app.after(100)

def on_click(event):
    animate_press()
    print("🎙️ Listening...")  # Replace this with your voice input start function

# Bind click event
canvas.tag_bind(sphere, "<Button-1>", on_click)

app.mainloop()
