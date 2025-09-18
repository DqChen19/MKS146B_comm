import serial
import time
from datetime import datetime

# Configure the serial port
serial_port = 'COM3'  # COM port
baud_rate = 9600     
parity = serial.PARITY_EVEN  
data_bits = 7         
stop_bits = serial.STOPBITS_ONE  
timeout = 1            

# MKS command to query data
query_command = b'@6021?\r'  # CR as terminator, check the manual for control protocol


start_time = datetime.now()
filename = f"./MKS_146B_Capacitance_Manometer/mks_data_{start_time.strftime('%Y%m%d_%H%M%S')}.txt"
#Change to local adress

# Open serial connection
try:
    ser = serial.Serial(
        port=serial_port,
        baudrate=baud_rate,
        parity=parity,
        stopbits=stop_bits,
        bytesize=data_bits,
        timeout=timeout
    )
    print(f"Connected to {serial_port}. Data will be saved to {filename}")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

# Continuously query data every second and save to the file
try:
    with open(filename, 'a') as file:
        while True:
            
            ser.write(query_command)
            response = ser.readline().decode('utf-8').strip()
            
            if response:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_entry = f"{timestamp} {response}\n"
                print(log_entry.strip())  # Print to console
                file.write(log_entry)    
            else:
                print("No response received. Check connection or command format.")

            # Wait 1 second before the next query
            time.sleep(60)
except KeyboardInterrupt:
    print("Stopping the script.")
finally:
    ser.close()
    print("Serial connection closed.")
