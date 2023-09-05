import pyautogui
import pathlib
import time

file_name = 'coordinates.txt'
local_path = pathlib.Path(__file__).parent
full_path = pathlib.Path.joinpath(local_path, file_name)

with open(full_path, 'r') as f:
	coordinates = f.read().splitlines()

for coordinate in coordinates:
	x, y = map(int, coordinate.split(' : '))
	pyautogui.moveTo(x, y)
	pyautogui.click()
	time.sleep(1)
