import tkinter
count = 0
time = 0

def countStart():
    global count
    global time

    label["text"] = str(count) + "초"
    count += 1
    time += 1
    if time > 4:
        return
    tk.after(1000, countStart)

tk = tkinter.Tk()
tk.title("연습")
tk.geometry("800x600")
button = tkinter.Button(text = "타이머시작", font = ("System", 30), command = countStart)
button.place(x=300, y=150)
label = tkinter.Label(tk, text = "0초", font = ("System", 45))
label.place(x=350, y=300)

tk.mainloop()