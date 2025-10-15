#making interface
import customtkinter as ctk
from PIL import Image
import voice_controlled as vc
import threading
import connector as cn
import voice_recog as vr


ctk.set_appearance_mode("dark")

main=ctk.CTk()
main.geometry("1200x720") 
main.title("VOICE ASSISTANT")
 

#importing mic image  
img=ctk.CTkImage(light_image=Image.open(r"D:\MINI PROJECT\main mini project\MINI-PROJECT\MIC2.png"),size=(100,100))
#displaying it
img_label = ctk.CTkLabel(main, image=img, text="",fg_color="black",corner_radius=100)
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

#making a system for voice recognition
def start_enrollment():
    output_label.configure(text=" Recording new voice sample...")
    
    def enroll_thread():
        path = vc.record_sample("new_voice.wav", duration=4)
        vr.enroll_user(path, "owner")
        output_label.configure(text=" Voice enrolled successfully. Click mic to verify.")
    
    threading.Thread(target=enroll_thread, daemon=True).start()

enroll_btn = ctk.CTkButton(
    main,
    text="Enroll New Voice",
    font=("Segoe UI Semibold", 18),
    command=start_enrollment,
)
enroll_btn.pack(pady=(30, 0))


#making the image a button
def mic_button():
    for scale in [0.9, 1.0]:  # shrink and restore
        new_size = int(100 * scale)
        new_img = ctk.CTkImage(light_image=Image.open(r"D:\MINI PROJECT\main mini project\MINI-PROJECT\MIC.png"), size=(new_size, new_size))
        img_label.configure(image=new_img)
        img_label.image = new_img
        main.update()
        main.after(100)



def start_listening():
    update_output(" Listening for verification...")
    temp_audio = vr.record_temp()  # record user's new input
    score, match = vr.verify_user(temp_audio, "owner")

    print(f"[DEBUG] Voice match: {match} | Score: {score}")

    if match:
        update_output(" Voice verified. Listening for commands...")
        result = vc.listen_once()  # your normal speech command function
        update_output(f"You said: {result}")

        # Send to ESP32
        if "on" in result.lower():
            cn.send_command("on")
            update_output(" Light turned ON")
        elif "off" in result.lower():
            cn.send_command("off")
            update_output(" Light turned OFF")
        else:
            update_output(" Command not recognized")

    else:
        update_output(" Voice not recognized. Access denied.")


# On mic click
def on_click(event=None):
    mic_button()
    threading.Thread(target=start_listening, daemon=True).start()


#binding the click
img_label.bind("<Button-1>",on_click)


main.mainloop()