import serial
import time

# Set the serial port and baud rate
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def send_integer_to_arduino(data):
    ser.write(str(data).encode('utf-8'))

try:
    while True:
        # Get user input or generate integer data
#         integer_data = int(input("Enter an integer to send to Arduino: "
        # Send the integer data to Arduinteger_dataino
        integer_data= 1 #stepper1 arm1
        send_integer_to_arduino(integer_data)
        print(f"Sent integer data to Arduino: {integer_data}")
        time.sleep(11)
        
        integer_data= 2#stepper2 arm2
        send_integer_to_arduino(integer_data)
        print(f"Sent integer data to Arduino: {integer_data}")
        time.sleep(11)
        
        integer_data= 3 #servo1 arm1
        send_integer_to_arduino(integer_data)
        print(f"Sent integer data to Arduino: {integer_data}")
        time.sleep(11)
        
        integer_data= 4 #servo2 arm2
        send_integer_to_arduino(integer_data)
        print(f"Sent integer data to Arduino: {integer_data}")
        time.sleep(11)
        
        integer_data= 5 #BO motor for both grippers
        send_integer_to_arduino(integer_data)
        print(f"Sent integer data to Arduino: {integer_data}")
        time.sleep(11)
        
        WP_data = ser.readline().decode().strip()
        print(f"Water pressure data: {WP_data}")
        
        
        
        

except KeyboardInterrupt:
    ser.close()
    print("Serial port closed")
