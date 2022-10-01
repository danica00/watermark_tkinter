import tkinter as tk
from tkinter import filedialog
# loading Python Imaging Library
from tkinter.filedialog import askopenfile
from tkinter.simpledialog import askstring

from PIL import ImageTk, Image, ImageFont, ImageDraw

# Create a window
#
# class Window:
#     def __init__(self, master):
#         self.pillow_image=Image.open("puppy.jpg")
#         self.image= ImageTk.PhotoImage(self.pillow_image)
#         self.label=tk.Label(master,image=self.image)
#         self.label.pack(padx=5,pady=5)
# root = tk.Tk()
# window = Window(root)
# root.mainloop()

root = tk.Tk()
root.title('Watermark')
# root.geometry('400x300')
# root.withdraw()
def file():
    file1 = askopenfile(mode='rb', filetypes=[('JPG File', '*.jpg'), ('PNG File', '*.png')])
    if file1 is not None:
        image1=Image.open(file1)
        watermark = tk.simpledialog.askstring(title='Watermark', prompt='Type your desired watermark')
        watermark_image = image1.copy()
        draw = ImageDraw.Draw(watermark_image)
        # ("font type",font size)
        font = ImageFont.truetype("arial.ttf", 50)
        # add Watermark
        # (0,0,0)-black color text
        draw.text((0, 0), watermark, (0, 0, 0), font=font)
        # add Watermark
        # (255,255,255)-White color text
        # draw.text((0, 0), "puppy", (255, 255, 255), font=font)
        test = ImageTk.PhotoImage(watermark_image)
        label1 = tk.Label(image=test)
        label1.image = test
        # label1 = tk.Label(image=test)
        # label1.image = test
        # # Position image
        # label1.pack(padx=5, pady=5)


        # Position image
        label1.pack(padx=5, pady=5)



frame = tk.Label(
    root,
    text='Chose a photo to add watermark',
    bg='#f0f0f0',
    font=(30)
)
frame.pack(expand=True)
open_button = tk.Button(root, text="Open Image", command=file)
open_button.pack()
root.mainloop()

# # Create a photoimage object of the image in the path
# image1 = Image.open("puppy.jpg")
# watermark_image = image1.copy()
# draw = ImageDraw.Draw(watermark_image)
# # ("font type",font size)
# font = ImageFont.truetype("arial.ttf", 50)
# # add Watermark
# # (0,0,0)-black color text
# draw.text((0, 0), "puppy", (0, 0, 0), font=font)
# # add Watermark
# # (255,255,255)-White color text
# # draw.text((0, 0), "puppy", (255, 255, 255), font=font)
# test = ImageTk.PhotoImage(watermark_image)
# label1 = tk.Label(image=test)
# label1.image = test
#
# # Position image
# label1.pack(padx=5, pady=5)
# root.mainloop()
