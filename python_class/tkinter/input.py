import tkinter

'''
def onClick():
    txt = en.get()
    button["text"] = txt

tk=tkinter.Tk()
tk.title("연습")
tk.geometry("800x600")
en = tkinter.Entry(width=20)# 텍스트 필드 작성
en.place(x=10, y= 10)

button = tkinter.Button(text = "버튼", command = onClick)
button.place(x=50, y=80)
tk.mainloop()
'''

def onClick():
    print("공격")
    txt = en.get()
    la["text"] = txt+"공격했습니다."

def onClick2():
    print("방어")
    txt = en.get()
    la["text"] = txt+"방어했습니다."

tk = tkinter.Tk()
tk.title("연습")
tk.geometry("800x600")

en = tkinter.Entry(width = 20)
en.place(x=10, y=10)
button = tkinter.Button(text = "공격", command = onClick)
button2 = tkinter.Button(text = "방어", command = onClick2)
button.place(x=50, y=80)
button2.place(x=100, y=80)
la = tkinter.Label(tk, text="대기", font="System, 24")
la.place(x=50, y=160)
tk.mainloop()