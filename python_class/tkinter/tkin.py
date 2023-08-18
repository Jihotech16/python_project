import tkinter

def onClick(): #클릭했을 
    button["text"] = "클릭"
    img2 = tkinter.PhotoImage(file = "Res3.png")
    canvas.create_image(250, 250, image=img2)
    canvas.image = img2

tk = tkinter.Tk() # 변수 선언
tk.title("GUI") # 윈도우창 제목
tk.geometry("800x600") # 윈도우창 크기

canvas = tkinter.Canvas(tk, width = 800, height = 600, bg ="Green")#캔버스 생성
canvas.pack() #캔버스 배치

img = tkinter.PhotoImage(file="Res2.png") # 이미지 변수(이미지 파일은 py 위치와 동일)
canvas.create_image(300, 200, image = img) # 이미지 캔버스에 그리기

label = tkinter.Label(tk, text="안녕하세요 ^^", font = ("System", 30))
#윈도우 객체, 라벨 이름, 폰트
label.place(x=250, y=0) # 라벨 위치 설정

button = tkinter.Button(tk, text="버튼", font = ("System", 30), command = onClick)# 버튼 지정
button.place(x=350, y=100) # 버튼 위치



tk.mainloop() # 계속 작동

