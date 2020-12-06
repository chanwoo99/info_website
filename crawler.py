

# 패키지 불러오기
import win32com.client
import os
# 엑셀 애플리케이션 준비



def exel2pdf(name):

    path= 'C:/Users/chanwoo/Desktop/python_web/info/food/'
    path_exel=path+name+".xlsx"
    path_pdf =path+name+".pdf"

    if os.path.isfile(path_pdf):
        os.remove(path_pdf)

    excel = win32com.client.Dispatch("Excel.Application")
    # 윈도우 화면에 띄울지, 아니면 백그라운드에서 돌릴지 선택
    # 테스트를 위해 True로 해서 직접 엑셀이 돌아가는 걸 눈으로 확인하자
    excel.Visible = True
    # 엑셀파일(워크북) 열기
    # 절대경로 입력!
    wb = excel.Workbooks.Open(path_exel)
    # 각 시트를 변수에 할당
    ws_data = wb.ActiveSheet

    # chart 시트 선택
    ws_data.Select()
    # pdf 저장경로, 파일명
    pdf_path = path_pdf
    # pdf 저장
    wb.ActiveSheet.ExportAsFixedFormat(0, pdf_path)
    # 워크북 종료 (저장하려면 True)
    wb.Close(False)
    # 엑셀 애플리케이션 종료
    excel.Quit()


exel2pdf("fd1")
exel2pdf("fd2")
exel2pdf("fd3")