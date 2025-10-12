#making interface
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")

main=ctk.CTk()
main.geometry("1200x720") 
main.title("VOICE ASSISTANT")

#importing sphere 
img=ctk.CTkImage(light_image=Image.open(r"D:/MINI PROJECT/main mini project/MINI-PROJECT/testsphere.jpg"),size=(100,100))
img_label = ctk.CTkLabel(main, image=img, text="")
img_label.pack(pady=250)

main.mainloop()