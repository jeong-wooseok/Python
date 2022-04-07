import pyautogui

# # 스크린샷 찍기 
# img = pyautogui.screenshot()
# img.save('screenshot.png')

# # 픽셀정보 가져오기
# pyautogui.mouseInfo()
# 669,194 30,30,30 #1E1E1E
# pixel = pyautogui.pixel(669,194)
# print(pixel)

pyautogui.pixelMatchesColor(669,194,(30,30,30))
# # 로그인 등 색상 변화 확인 후 작업을 진행하고자 할때 픽셀매칭메소드 활용