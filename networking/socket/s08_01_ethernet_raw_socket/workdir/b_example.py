import socket

ETH_P_ALL = 3

ETH_FRAME_LEN = 1514  # Max. octets in frame sans FCS

interface = 'eth0'

s = socket.socket(
    socket.AF_PACKET,
    socket.SOCK_RAW,
    socket.htons(ETH_P_ALL)
)

s.bind((interface, 0,))

data = s.recv(ETH_FRAME_LEN)

print(data)  # => b'\x08\x00\x27\xdd\xd7\x43\x08\x00\x27\x8e\x75\x44\x88\xb5Hi'

s.close()
