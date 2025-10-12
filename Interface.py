#making interface
import customtkinter as ctk
from PIL import Image
import voice_controlled as vc
import threading

ctk.set_appearance_mode("dark")

main=ctk.CTk()
main.geometry("1200x720") 
main.title("VOICE ASSISTANT")

#importing sphere 
img=ctk.CTkImage(light_image=Image.open(r"D:/MINI PROJECT/main mini project/MINI-PROJECT/testsphere.jpg"),size=(100,100))
#displaying it
img_label = ctk.CTkLabel(main, image=img, text="")
img_label.pack(pady=250)

# Label to show text output
output_label = ctk.CTkLabel(main, text="Click the mic to start listening", font=("Arial", 16))
output_label.pack(pady=200)


#making the image a button
def mic_button():
    for scale in [0.9, 1.0]:  # shrink and restore
        new_size = int(100 * scale)
        new_img = ctk.CTkImage(light_image=Image.open(r"D:\MINI PROJECT\main mini project\MINI-PROJECT\testsphere.jpg"), size=(new_size, new_size))
        img_label.configure(image=new_img)
        img_label.image = new_img
        main.update()
        main.after(100)

#funtion to start listening
def start_listening_thread():
    threading.Thread(target=start_listening, daemon=True).start()

#on clicking 
def on_click(event=None):
    mic_button()
    output_label.configure(text="🎙️ Listening... Please speak now.")
    vc.listen_command()

#binding the click
img_label.bind("<Button-1>",on_click)


main.mainloop()