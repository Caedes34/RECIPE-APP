from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Text
import requests
from PIL import Image, ImageTk
from io import BytesIO
import webbrowser
from playsound import playsound  # Ensure you have this module
from py_edamam import PyEdamam  # Ensure you import your recipe fetching class

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Downloads\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("747x504")
window.configure(bg = "#A46D6D")


canvas = Canvas(
    window,
    bg = "#A46D6D",
    height = 504,
    width = 747,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 5, y = 0)
canvas.create_text(
    122.0,
    210.0,
    anchor="nw",
    text="Then What do you want?",
    fill="#CC9318",
    font=("Montserrat Bold", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    372.0,
    280.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=140.0,
    y=262.0,
    width=466.0,
    height=35.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_search.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg="#D9D9D9",  # Set to match the canvas background color
    activebackground="#A46D6D",  # Set to match the canvas background color
    bd=0,  # Set border width to 0
    padx=0,  # Remove horizontal padding
    pady=0   # Remove vertical padding
)
button_1.place(
    x=575.0,
    y=261.56,
    width=45.0,
    height=36.0
)




window.resizable(False, False)
window.mainloop()