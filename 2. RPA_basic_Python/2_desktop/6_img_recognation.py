import pyautogui
# bin_button = pyautogui.locateOnScreen('bin.png')
# # print(bin_button)
# pyautogui.click(bin_button)

# # 다수의 이미지를 차례로 작업하는 경우
# # (아래 주소의 창을 우측에 띄우고 실습)
# # https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox
# for i in pyautogui.locateAllOnScreen('cbox.png'):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# # 속도개선
# # 1. GrayScale
# bin_button = pyautogui.locateOnScreen('bin.png', grayscale=True)
# print(bin_button)

# # 2. 범위지정
# # pyautogui.mouseInfo()
# # 1000,800 30,30,30 #1E1E1E
# # 546,447 30,30,30 #1E1E1E
# bin_button = pyautogui.locateOnScreen('bin.png', region=(546,447,464,353))
# pyautogui.moveTo(bin_button)

# 3. 정확도 조정
# 설치 : pip install opencv-python
bin_button = pyautogui.locateOnScreen('bin.png', confidence=0.9)
pyautogui.moveTo(bin_button)