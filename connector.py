# Modified connector.py

import serial
import time 

# --- CONFIGURATION: CHANGE THIS PORT ---
ESP32_PORT = 'COM4'  # <<< CONFIRM/CHANGE YOUR ESP32's COM PORT (e.g., 'COM3', '/dev/ttyUSB0')
BAUD_RATE = 115200
# ---------------------------------------

def send_command(cmd):
    """Opens, sends command, and closes serial connection to ESP32."""
    try:
        # The serial connection is opened inside the function to ensure the port is fresh for each command
        esp = serial.Serial(ESP32_PORT, BAUD_RATE, timeout=1)  
        time.sleep(0.1)  # A short delay after opening the port
        
        # Ensure command is 'ON' or 'OFF' and encode for serial
        serial_cmd = cmd.upper()
        esp.write((serial_cmd + "\n").encode())
        print(f"Sent to ESP32: {serial_cmd}")
        
        # Read response from ESP32 to confirm receipt (optional but recommended)
        response = esp.readline().decode('utf-8').strip()
        if response:
            print(f"ESP32 Response: {response}")
             
        esp.close()
    except Exception as e:
        print(f"Error sending command via Serial on {ESP32_PORT}: {e}")