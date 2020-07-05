# import serial
import crc
import time
import struct
from reg_defs import *
from bitstring import BitArray
import yaml
import os

# SERIAL_PORT = os.getenv('SERIAL_PORT', "COM4")

# baudrate = 115200
# anticollision_time = 3*80*1000/baudrate / 1000;

# ser = serial.Serial(SERIAL_PORT, baudrate, timeout=0, rtscts=True, dsrdtr=True)

baudrate = 115200
anticollision_time = 3*80*1000/baudrate / 1000;

def get_bits(bytearr,idx,length=1):
    bits = BitArray(bytearr)
    return bits[len(bits)-idx-length:len(bits)-idx].uint

    
def create_read_datagram(register_addr):
    datagram = bytearray([TMC2208_SYNC, TMC2208_SLAVE_ADDR, TMC2208_READ|register_addr])
    datagram.append(crc.crc8atm(datagram))
    # print("Send: " + str(datagram))
    return datagram


def create_write_datagram(register_addr, data):
    datagram = bytearray([TMC2208_SYNC, TMC2208_SLAVE_ADDR, TMC2208_WRITE|register_addr, data[3], data[2], data[1], data[0]])
    datagram.append(crc.crc8atm(datagram))
    # print("Send: " + str(datagram))
    return datagram

def read_data(ser):
    data = ser.readline()
    while len(data) >= 4:
        if data[0] == 0x05:
            if data[1] == 0: # Echo
                if data[2] & 0x80:  # Write request
                    if len(data) >= 8:
                        data = data[8:]
                    else:
                        return
                else:
                    data = data[4:]
            else: # Data to decode
                if len(data) >= 8:
                    datagram = data[:8]
                    data = data[8:]
                    return decode_datagram(datagram)
                else:
                    return
        else:
            data = data[1:]

def decode_datagram(datagram):
    addr = datagram[2]
    rawdata = datagram[3:-1]
    register_def = next(r for r in registers if r["addr"] == addr)

    data = {register_def["name"]: {bit_def["name"]: get_bits(rawdata, bit_def["bit"], bit_def["len"]) for bit_def in register_def["bit_name"]}}

    return data

def write_register(ser, addr, data):
    ser.write(create_write_datagram(addr, data))

def read_regsiter(ser, addr):
    ser.write(create_read_datagram(addr))
    time.sleep(anticollision_time)
    return read_data(ser)

def read_all(ser):
    register_data = {}
    for register in registers:
        if register["rw_info"] != "W":
            register_data = {**register_data, **read_regsiter(ser, register["addr"])}

    # print(yaml.dump(register_data, default_flow_style=False))
    return register_data


# time.sleep(0.1)
# ser.write(create_read_datagram(REG_GCONF))
# time.sleep(anticollision_time)
# read_data()
# read_all()