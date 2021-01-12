from openpyxl import Workbook

wb = Workbook() # 새 워크북 생성
ws = wb.active # 현재 활성화된 sheet 가져옴
ws.title ='twbly' # 워크시트 이름 설정
wb.save('sample.xlsx') # sheet 의 이름을 변경
wb.close()

