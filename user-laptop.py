import asyncio
import websockets
import json

async def send_command(command):
    uri = "ws://192.168.83.21:8765"  # Replace with Pico’s IP
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"command": command}))
        print(f"Sent: {command}")
    

asyncio.run(send_command("move_car"))  # Pico should move left