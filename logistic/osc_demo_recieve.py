from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc.osc_server import BlockingOSCUDPServer

def print_handler(address, *args):
    print(f"{address}: {args}")

disp = dispatcher.Dispatcher()
disp.map("/logistic", print_handler)

ip = "127.0.0.1"
port = 12345

server = BlockingOSCUDPServer((ip, port), disp)  # Use 'disp' here instead of 'dispatcher'
server.serve_forever()  # Blocks forever
