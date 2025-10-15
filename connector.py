import serial
import time 
def send_command(cmd):
    try:
        esp = serial.Serial('COM4', 115200, timeout=1)  # Change COM5 to your port
        time.sleep(2)  # give ESP time to reset
        esp.write((cmd + "\n").encode())
        print(f"Sent to ESP32: {cmd}")
        esp.close()
    except Exception as e:
        print("Error:", e)
