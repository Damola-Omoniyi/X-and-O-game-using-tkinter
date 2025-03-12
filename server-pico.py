from ws import WS_Server
import json
import time
import pico_4wd as car


# Custom WebSocket Server Class
class CustomWSServer(WS_Server):
    def on_receive(self, data):
        print(f"Received: {data}")  # Debugging
        if isinstance(data, dict) and "command" in data:
            cmd = data["command"]
            if len(cmd) == 2 and cmd[0] in ["left", "right", "forward", "backward"]:
                car.move(cmd[0], cmd[1])
            elif cmd[0] in ["stop", "STOP"]:
                car.move("stop")
            
            

# Initialize WebSocket Server
ws = CustomWSServer(name="PicoW", mode="sta", ssid="Damola's A05s", password="Overdose")

if ws.start():
    print("WebSocket server running...")

# Run WebSocket Loop
while True:
    ws.loop()
    time.sleep(0.1)  # Prevent CPU overload
