from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder
import time
IP = '10.249.30.241'
PORT = 12345

def logistic_map(r, x):
    return r * x * (1 - x)

r = 3.9  # Control parameter
x = 0.5  # Initial value

client = udp_client.UDPClient(IP, PORT)

while True:
    msg = OscMessageBuilder(address='/logistic')
    x = logistic_map(r,x)
    msg.add_arg(x)
    m = msg.build()
    client.send(m)
    print(x)
    time.sleep(0.1)