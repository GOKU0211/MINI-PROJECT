#making interface
import customtkinter as ctk
from PIL import Image
import voice_controlled as vc
import threading
import connector as cn

ctk.set_appearance_mode("dark")

main=ctk.CTk()
main.geometry("1200x720") 
main.title("VOICE ASSISTANT")

#importing sphere 
img=ctk.CTkImage(light_image=Image.open(r"D:\MINI PROJECT\main mini project\MINI-PROJECT\MIC.png"),size=(100,100))
#displaying it
img_label = ctk.CTkLabel(main, image=img, text="")
img_label.pack(pady=(100, 20))


# Label to show text output 
output_label = ctk.CTkLabel(
    main,
    text="Click the mic to start listening",
    font=("Segoe UI Semibold", 18),
    text_color="#00FFFF",  # cyan glow style
)
output_label.pack(pady=(20, 0))

# Function to update label (this replaces print)
def update_output(message):
    output_label.configure(text=message)

# Connect GUI callback to voice module
vc.update_callback = update_output


#making the image a button
def mic_button():
    for scale in [0.9, 1.0]:  # shrink and restore
        new_size = int(100 * scale)
        new_img = ctk.CTkImage(light_image=Image.open(r"D:\MINI PROJECT\main mini project\MINI-PROJECT\MIC.png"), size=(new_size, new_size))
        img_label.configure(image=new_img)
        img_label.image = new_img
        main.update()
        main.after(100)




#funtion to start listening
def start_listening_thread():
    threading.Thread(target=start_listening, daemon=True).start()
def start_listening():
    output_label.configure(text=" Listening...")
    result=vc.listen_once()
    output_label.configure(text=result)

    #connecting to esp32
    cn.send_command(result.lower())

#on clicking 
def on_click(event=None):
    mic_button()
    output_label.configure(text=" Listening... Please speak now.")
    threading.Thread(target=vc.listen_once,daemon=True).start()



#binding the click
img_label.bind("<Button-1>",on_click)


main.mainloop()