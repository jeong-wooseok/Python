import pyautogui

pyautogui.moveTo(200,100,duration=0.5) # 절대좌표로 이동
pyautogui.moveTo(100,200, duration=0.5) # 0.5초동안 100,200으로 이동

p=pyautogui.position()
pyautogui.move(100,100,duration=0.5) # 상대좌표로 이동
print(p)
pyautogui.move(100,100,duration=0.5) 
print(p)
pyautogui.moveTo(100,100,duration=0.5) # 절대좌표로 이동
print(pyautogui.position())