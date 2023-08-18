import tkinter
'''
tk=tkinter.Tk()
tk.title("연습")
tk.geometry("400x300")
val = tkinter.BooleanVar()
val.set(True)#체크박스 상태를 True로 세팅
checkbutton = tkinter.Checkbutton(text="체크버튼", variable = val)#체크버튼 선언
checkbutton.pack()#체크버튼 정의 및 배치
if val.get() == True:
    print("체크되었습니다.")
else:
    print("해제되었습니다.")
tk.mainloop()
'''

tk=tkinter.Tk()
tk.title("구구단 퀴즈")
tk.geometry("400x600")

def onClick():
    if val1.get() and val2.get() == True:
        print("둘 중 하나를 선택해주세요.")
        label3["text"] = "하나만 골라주세요"
    else:
        if val1.get() or val2.get() == False:
            print("안고름")
            label3["text"] = "답을 골라주세요."
        if val1.get() == True:
            print("정답입니다.")
            label3["text"]= "정답입니다."
        if val2.get() == True:
            print("틀렸습니다.")
            label3["text"]= "오답입니다."


canvas = tkinter.Canvas(tk, width = 400, height = 600, bg = "green")
canvas.pack()
val1 = tkinter.BooleanVar()
val1.set(False)
val2 = tkinter.BooleanVar()
val2.set(False)
label1 = tkinter.Label(tk, text = "다음 중 옳은 것은?", font = ("System", 30), bg = "green")
label1.place(x=90, y=20)
label2 = tkinter.Label(tk, text = "3x9=?", font = ("System", 30))
label2.place(x=150, y=80)
label3 = tkinter.Label(tk, text = "", font=("System", 40), bg = "green")
label3.place(x=100, y = 300)
check1 = tkinter.Checkbutton(text = "27", variable=val1)
check2 = tkinter.Checkbutton(text = "26", variable=val2)
check1.place(x=150, y= 150)
check2.place(x=200, y= 150)
button = tkinter.Button(tk, text = "정답확인",font = ("System", 30), command = onClick)
button.place(x=150, y= 200)
tk.mainloop()
