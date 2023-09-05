from pynput.mouse import Listener
import pathlib

coordinates = [] 

file_name = 'coordinates.txt'
local_path = pathlib.Path(__file__).parent
full_path = pathlib.Path.joinpath(local_path, file_name)

def on_click(x, y, button, pressed):
    if pressed:
        coordinates.append(f"{int(x)} : {int(y)}")
        print(f"{x}, {y}")

try:
	with Listener(on_click=on_click) as listener:
		print("\n\nRecording mouse clicks. Press Ctrl+C to stop.")
		listener.join()
		
except KeyboardInterrupt:
	print("\n\nRecorded Coordinates:")
	print(coordinates)

with open(full_path, 'a') as f:
	f.write('\n'.join(coordinates))

