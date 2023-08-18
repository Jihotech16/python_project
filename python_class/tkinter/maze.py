import tkinter
import winsound

keyInput = ""#키 입력 전역변수 선언
def key_Down(i): #키를 입력할 때
    global keyInput
    keyInput = i.keysym#입력한 키의 이름
    print(keyInput)

def key_Up(i): #키를 입력하고 뗐을 때
    global keyInput
    keyInput = ""#키 값을 다시 초기화
'''
def playerMove():
    global posX, posY
    if keyInput == "Up":
        posY -= 1
    if keyInput == "Down":
        posY += 1
    if keyInput == "Right":
        posX += 1
    if keyInput == "Left":
        posX -= 1
'''

def main_Game():
    global posX, posY
    global isItem
    if itemX - posX < 1 and itemY - posY < 1 and isItem == 0:
        canvas.delete("item")
        winsound.PlaySound("coin.wav", winsound.SND_ASYNC)
        isItem = 1
        canvas.create_rectangle(50, 50, 200, 200, fill = "green")
    
    canvas.coords("player", posX*50 + 70, posY*50 + 70)
    tk.after(100, playerMove)


key = 0
isItem = 0
#position 값 초기화
posX = 0
posY = 0

itemX = 500
itemY = 500
tk = tkinter.Tk()
tk.title("maze")
tk.geometry("800x600")
tk.bind("<KeyPress>", key_Down)
tk.bind("<KeyRelease>", key_Up)
canvas = tkinter.Canvas(width = 800, height = 600, bg = "black")

#canvas.create_rectangle(50, 50, 200, 200, fill = "red", outline = "green", width = 10)

canvas.pack()
gameMap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
for y in range(7):
    for x in range(10):
        if gameMap[y][x] == 1:
            canvas.create_rectangle(x*50, y*50, x*50+50, y*50+50, fill = "green", outline = "red", width = 5)

img = tkinter.PhotoImage(file = "rabbit.png").subsample(10)
im2 = tkinter.PhotoImage(file = "rabbit.png").subsample(20)
canvas.create_image(posX*50 + 70, posY*50 + 70, image = img, tag = "player")
canvas.create_image(itemX, itemY, image = im2, tag = "item")
main_Game()
tk.mainloop()