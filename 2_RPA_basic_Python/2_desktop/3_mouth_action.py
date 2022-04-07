import pyautogui
pyautogui.sleep(3)
# print(pyautogui.position())

# # 클릭
# pyautogui.click(117,14,duration=0.5) #0.5초동안 해당위치로 이동 후 클릭
# pyautogui.click() # 클릭
# pyautogui.mouseDown() # 클릭상태로 눌러둠
# pyautogui.mouseUp() # 클릭상태에서 해제
# pyautogui.click(clicks=2) # 더블클릭
# pyautogui.rightClick() # 우클릭
# pyautogui.click(clicks=300, duration=2) # 다수클릭


# # 그림판에서 테스트
# pyautogui.moveTo(200,200,duration=0.5)
# pyautogui.mouseDown() 
# pyautogui.moveTo(300,300,duration=0.5)
# pyautogui.mouseUp()

# # 열려있는 창 드래그
# print(pyautogui.position()) # 드래그하고자 하는 창위 위치 확인
# pyautogui.moveTo(1088,488)
# pyautogui.drag(200,100,duration=0.5)
# pyautogui.moveTo(1288,588)
# pyautogui.dragTo(200,100,duration=0.5)

# 스크롤
pyautogui.scroll(-300) #양수이면 위 방향으로, 음수이면 아래방향으로 스크롤







