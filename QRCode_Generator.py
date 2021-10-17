from tkinter import *

# from tkinter import ttk
import pyqrcode
from pyqrcode import *
import png
# from pyzbar.pyzbar import decode
from PIL import Image


window = Tk()
window.title("QRCode Generator")
window.geometry("600x600")
window.configure(bg="#000000")


def create_code():
    code = pyqrcode.create(url_input.get())
#    code.save("filename.png")
    code.png(f"{code}", scale=8)
#    d = decode(Image.open("google.png"))
    print(code)

# def save_code():


url_input = StringVar()
url_input.set("Insert your URL")
url = Entry(window, textvariable=url_input, justify="center")
url.configure(width="20")
url.pack()

generate = Button(window, text="Generate")
generate.configure(width="20", height="2", bg="#25A8F5", command=create_code)
generate.pack()


window.mainloop()
