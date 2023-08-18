import tkinter
import tkinter.messagebox #메시지 박스 모듈 가져오기

def chlick():
    tkinter.messagebox.showinfo("메시지", "버튼클릭")
                                #타이틀 , 내용

tk = tkinter.Tk()
tk.title("연습")
tk.geometry("800x600")

button = tkinter.Button(tk, text = "버튼", font = "System, 24", command = chlick)
button.pack()
tk.mainloop()