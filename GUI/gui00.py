from tkinter import *
from tkinter import messagebox

root = Tk()
btn01 = Button(root)
btn01["text"] = "点我"
btn01.pack()


def aini(e):
    messagebox.showinfo("Message", "我爱你")
    print("I love you")  # 控制台打印


btn01.bind("<Button-1>", aini)  # 事件绑定

root.mainloop()  # 调用组件的mainloop()方法,进入事件循环