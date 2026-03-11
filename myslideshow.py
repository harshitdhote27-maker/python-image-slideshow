import tkinter as tk
import time
from PIL import Image,ImageTk  # image resize and then we convert the image in imagetk

#Main window
root=tk.Tk()
root.title("Tech-Ard-pi32 private innovation library")
root.geometry("900x900")


# list of the image paths
image_paths=[
   r"C:\Users\Dell\Desktop\Campus Buddy 2 (1)/image0.jpeg",
   r"C:\Users\Dell\Desktop\Campus Buddy 2 (1)/image1.jpeg",
   r"C:\Users\Dell\Desktop\Campus Buddy 2 (1)/image3.jpeg",
   
   
]
image_size=(700,700)
images=[]
for path in image_paths:
    img=Image.open(path)
    img=img.resize(image_size)
    images.append(img) #adding each image in this list

#convert PIL image into Tkinter compatible image
# 
final_images=[]
for img in images:
   photo=ImageTk.PhotoImage(img) #convert 
   final_images.append(photo)

# label widget to keep photoum 
image_label=tk.Label(root)
image_label.pack(pady=30)

#slideshow  funcation
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)

#button
play_button=tk.Button(
    root,
    text="play the slideshow",
    font=("Arial",17),
    command=start_slideshow
)        

play_button.pack(pady=40)
root.mainloop()