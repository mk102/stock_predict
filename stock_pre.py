#!/usr/bin/python3
# -*- coding: utf8 -*-
import tkinter as tk
import jup_pre
from tkinter.ttk import *

#def pushed(self,value):
 #self["text"] = "aaa"



#rootウィンドウを作成
root = tk.Tk()
#rootウィンドウのタイトルを変える
root.title("株価予測アプリ")
#rootウィンドウの大きさを320x240に
root.geometry("500x300")

label = tk.Label(text="会社名：")
label.place(x=10, y=25)
#エントリー
#EditBox = tk.Entry(width=10)
#EditBox.place(x=100,y=20)

comboBox = Combobox(root, width=10, state="readonly", values=("ソフトバンク", "トヨタ自動車", "任天堂"))
comboBox.place(x=100,y=20)

def make(event):
    #ここで，valueにEntryの中身が入る
    sele = comboBox.get()
    if sele == "ソフトバンク":
        firm = "SFTBF"
    elif sele == "トヨタ自動車":
        firm = "TOYOF"
    elif sele == "任天堂":
        firm = "NTDOF"
    value = jup_pre.samp(firm)
    value = sele + "の" + value
    label = tk.Label(text=value)
    label.place(x=50, y=100)
#Label部品を作る
#label = tk.Label(root, text="Tkinterのテストです")
#表示する
#label.grid()

#ボタンを作る
#button = tk.Button(root, text="ボタン", command= lambda : pushed(button))
#表示
#button.grid()

button1 = tk.Button(root, text='予測開始',width=10)
button1.bind("<Button-1>",make)
button1.place(x=220, y=25)
#button1.pack(x=20, y=5)



#メインループ
root.mainloop()
