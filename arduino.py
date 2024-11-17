import serial
import serial.tools.list_ports
import time
import streamlit as st
# import streamlit as st
flag = 0

gas = [0]
temp = [0]
hum = [0]
tds = [0]
times = [0]

time_increment = 2  # Increment for time values
max_time_window = 25  # Maximum time window to display on the graph


def all_values():
    global flag , Ard
    # radar_value = [0, 0]
    tries = 0
    while True:
        if flag == 0 :
            try : 
                port = "COM9"
                Ard = serial.Serial(port, 9600)
                time.sleep(2)
                flag = 1

                break
            except :
                flag = 0
                st.rerun()
        #         if tries <= 20:
        #             print("Try ",tries)
        #             tries += 1
        #             time.sleep(1)
        #             continue
        #         else :
        #             exit()
        else:
            break
    
    while True:
        myData = Ard.readline().decode().strip()
        data = myData.split(",")
        print(data)
        if len(data) == 12:
            if (data[1]).isdigit():
                gas.append(int(data[7]))
                temp.append((int(data[5])-5))
                hum.append(int(data[3]))
                tds.append(int(data[1]))
                angle = int(data[9])
                dist = int(data[11])
                # times.append((times[-1])+1)
                times.append(times[-1] + time_increment)
                # print(data)
                radar_value = [angle, dist]
                print(radar_value)
                if len(times) > max_time_window // time_increment: #To remove old values from the data list
                    gas.pop(0)
                    temp.pop(0)
                    hum.pop(0)
                    tds.pop(0)
                    times.pop(0)
        break
    return gas,temp,hum,tds,times,radar_value

def send_command(command):
    Ard2.write((command + '\n').encode('utf-8'))  # Send the command to the Arduino
    # time.sleep(0.1)  # Give the Arduino some time to process the command
    # if Ard2.in_waiting > 0:
    #     response = Ard2.readline().decode('utf-8').rstrip()
    #     print(response)

flag_2 = 0
def laser_control(status):
    global flag_2,Ard2
    while True:
        if flag_2 == 0 :
            try : 
                port2 = "COM10"
                Ard2 = serial.Serial(port2, 9600)
                flag_2 = 1
                print("connected")
                break
            except :
                pass
        else:
            break

    # port = "COM6"
    # # Ard = serial.Serial(port, 9600)
    
    if status == 1:
        print("openlaser")
        send_command('openlaser')
    elif status == 0:
        print("closelaser")
        send_command('closelaser')
    elif status == 2:
        print("Opening door")
        send_command('open')

def auth():
    global flag_2,Ard2
    while True:
        if flag_2 == 0 :
            try : 
                port2 = "COM6"
                Ard2 = serial.Serial(port2, 9600)
                flag_2 = 1
                print("connected")
                break
            except :
                pass
        else:
            break
    while True:
        response = Ard2.readline().decode('utf-8').rstrip()
        time.sleep(0.05)
        print(response)
        if response == 'Authorized access':
            return response
        
        elif response == 'Access denied':
            return response


    





