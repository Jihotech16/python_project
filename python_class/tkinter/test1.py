import tkinter
import random

def ClickButton():
    label["text"]=random.choice(["후라이드치킨", "양념치킨", "반반치킨", "간장치킨"])

tk = tkinter.Tk()
tk.title("치킨메뉴 선택")
tk.geometry("1280x760")#해상도 선택

canvas = tkinter.Canvas(tk, width = 800, height = 600) #캔버스 크기
canvas.pack()

bgImage = tkinter.PhotoImage(file = "chicken.png")
canvas.create_image(400, 300, image = bgImage)

label = tkinter.Label(tk, text = "치킨", font =("System", 40), fg = "white")
label.place(x=500, y=100)

button =tkinter.Button(text = "치킨메뉴뽑기", font=("System", 30), fg = "red", command = ClickButton)
button.place(x=480, y=550)

tk.mainloop()