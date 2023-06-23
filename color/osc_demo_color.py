from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder
import random

IP = '127.0.0.1'
PORT = 12345

client = udp_client.UDPClient(IP, PORT)

while True:
    
    msg = OscMessageBuilder(address='/color')
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)

    msg.add_arg(R)
    msg.add_arg(G)
    msg.add_arg(B)

    m = msg.build()
    print(m)
    client.send(m)