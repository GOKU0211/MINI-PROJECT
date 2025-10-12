#making interface
import customtkinter as ctk
from PIL import Image
import voice_controlled as vc
ctk.set_appearance_mode("dark")

main=ctk.CTk()
main.geometry("1200x720") 
main.title("VOICE ASSISTANT")

#importing sphere 
img=ctk.CTkImage(light_image=Image.open(r"D:/MINI PROJECT/main mini project/MINI-PROJECT/testsphere.jpg"),size=(100,100))
#displaying it
img_label = ctk.CTkLabel(main, image=img, text="")
img_label.pack(pady=250)

#making the image a button
def mic_button():
    for scale in [0.9, 1.0]:  # shrink and restore
        new_size = int(100 * scale)
        new_img = ctk.CTkImage(light_image=Image.open(r"D:\MINI PROJECT\main mini project\MINI-PROJECT\testsphere.jpg"), size=(new_size, new_size))
        img_label.configure(image=new_img)
        img_label.image = new_img
        main.update()
        main.after(80)

#on clicking 
def on_click(event=None):
    mic_button()
    vc.listen_command()

#binding the click
img_label.bind("<Button-1>",on_click)


main.mainloop()