import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog, ttk
# loading Python Imaging Library
from tkinter.filedialog import askopenfile
from tkinter.simpledialog import askstring

from PIL import ImageTk, Image, ImageFont, ImageDraw

root = tk.Tk()
root.title('Watermark')
root.resizable=True


def file():
    def add_watermark():
        watermark_image = image1.copy()
        width,height = watermark_image.size
        draw = ImageDraw.Draw(watermark_image)
        # ("font type",font size)
        font = ImageFont.truetype("arial.ttf", 15)
        # add Watermark
        # (0,0,0)-black color text
        draw.text((width-width+20, height-40), "Customize Watermark©", (220, 220, 220), font=font)
        # add Watermark
        # (255,255,255)-White color text
        # draw.text((0, 0), "puppy", (255, 255, 255), font=font)
        test1 = ImageTk.PhotoImage(watermark_image)
        label1.config(image=test1)
        def customize():

            text = tk.simpledialog.askstring(title='Watermark txt', prompt="Enter your watermark test")
            # font1= f'{tk.simpledialog.askstring(title="Choose font", prompt="Enter your desired font")}.ttf'

            watermark_image1 = image1.copy()
            draw1 = ImageDraw.Draw(watermark_image1)
            draw1.text((width-width+20, height-40), text, (220, 220, 220), font=font)

            test2 = ImageTk.PhotoImage(watermark_image1)
            label1.config(image=test2)
            root.mainloop()

        # Change browse button text to add customize watermark
        customize_text = tk.StringVar()
        browse_btn.config(command=customize, textvariable=customize_text)

        customize_text.set("Customize watermark")

        # # Position image
        label1.grid(column=3, row=0)
        root.mainloop()


    file1 = askopenfile(mode='rb', filetypes=[('JPG File', '*.jpg'), ('PNG File', '*.png')])
    if file1 is not None:
        image1 = Image.open(file1)

        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.image = test

        # Position image
        label1.grid(column=3, row=0)
        instruction_label.config(text="Add watermark")
        # Change browse button to add watermark button
        watermark_text = tk.StringVar()
        browse_btn.config(command=add_watermark, textvariable=watermark_text)

        watermark_text.set("Add watermark")

        root.mainloop()

#starts here:
canvas = tk.Canvas(root, width=600, height=500)
canvas.grid(columnspan=5, rowspan=4)



logo = Image.open("Watermark it.png")
logo = logo.resize((200, 200))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.grid(column=3, row=0)

instruction_label = tk.Label(root, text="Select photo to watermark.", font="Ariel")
instruction_label.grid(columnspan=5, column=0, row=1)

# Browse dialog button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, command=file, textvariable=browse_text, font="Ariel", bg="#20bebe", fg="white",
                       height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=2)

# Success Message
success_text = tk.StringVar()
success_text.set(" ")
success_label = tk.Label(root, textvariable=success_text)
success_label.grid(columnspan=5, column=0, row=3)

# Cancel Button
cancel_btn = tk.Button(root, text="Quit", command=quit, font="Ariel", bg="#20bebe", fg="white", height=2, width=15)
cancel_btn.grid(column=4, row=2, padx=10)
frame = tk.Label(
    root,
    text='Chose a photo to add watermark',
    bg='#f0f0f0',
    font=(30)
)

root.mainloop()


