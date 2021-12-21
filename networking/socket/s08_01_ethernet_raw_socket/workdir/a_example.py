import uuid
import socket

from mac_utils import mac_string_to_bytes as mac_convert

ETH_P_ALL = 3

interface = 'eth0'

dst = mac_convert("02:42:ac:10:00:09")  # destination MAC address
src = uuid.getnode().to_bytes(6, 'big')  # source MAC address

proto = b'\x88\xb5'                # ethernet frame type
payload = 'Hi'.encode()            # payload

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
s.bind((interface, 0,))

s.sendall(dst + src + proto + payload)

s.close()
