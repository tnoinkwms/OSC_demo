import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pythonosc import dispatcher, osc_server
from threading import Thread
from matplotlib.animation import FuncAnimation

class OSCServerThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.daemon = True
        self.latest_rgb = None

        def handler(address, *args):
            self.latest_rgb = args  # Save received RGB values.

        disp = dispatcher.Dispatcher()
        disp.map("/color", handler)
        self.server = osc_server.ThreadingOSCUDPServer((ip, port), disp)

    def run(self):
        self.server.serve_forever()

    def get_latest_rgb(self):
        return self.latest_rgb

# Start OSC server in a new thread.
osc_thread = OSCServerThread("127.0.0.1", 12345)
osc_thread.start()

# Initialize plot.
fig, ax = plt.subplots(1)
plt.axis('off')
patch = patches.Rectangle((0, 0), 1, 1, transform=ax.transAxes)
ax.add_patch(patch)

# Update plot.
def update(frame):
    rgb = osc_thread.get_latest_rgb()
    if rgb is not None:
        patch.set_facecolor([v/255 for v in rgb])  # Set patch color.
    return patch,

ani = FuncAnimation(fig, update, interval=100)
plt.show()
