def crc8atm(datagram):
    crc = 0;
    for i in range(len(datagram)):
        current_byte = datagram[i]
        for j in range(8):
            if (crc >> 7) ^ (current_byte & 0x01):
                crc = (crc << 1) ^ 0x07
            else:
                crc = (crc << 1)

            crc = crc & 0xff
            current_byte = current_byte >> 1
    return crc