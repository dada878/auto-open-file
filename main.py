#import mod
import tkinter as tk
import os
import tkinter.messagebox
from tkinter import Tk, filedialog
import subprocess
import time

#window start and set values
window = tk.Tk()
window.title('自動開啟檔案')
window.geometry("100x130")

file_path = ""

#function
def alert(msg):
    tkinter.messagebox.showinfo(title = '提示', message = msg)

def openfile():
    global file_path
    path_test = filedialog.askopenfilename()
    if path_test != "":
        file_path = path_test
    textpath['text']=file_path.split("/")[len(file_path.split("/"))-1]

def OPENFILE(timetick):
    window.destroy()
    time.sleep(timetick*60)
    subprocess.call(file_path, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def check_and_run():
    if (file_path=="" or file_path=="尚未選擇檔案"):
        alert("請先選擇檔案")
        return
    try:
        int(backup_time.get())
    except:
        alert("請輸入正確的時間")
        return
    alert("設定成功(接下來為背景作業)\n將在"+backup_time.get()+'分鐘後開啟"'+file_path.split("/")[len(file_path.split("/"))-1]+'"')
    OPENFILE(int(backup_time.get()))
    
#set window
ap = tk.Label(window, text='設定時間(分)')
ap.grid(row=0)

backup_time = tk.Entry(window,width=15)
backup_time.grid(row=1,padx=5,pady=5)

btnn = tk.Button(text="選擇檔案",command=openfile)
btnn.grid(row=2,ipadx=25)

textpath = tk.Label(window, text='尚未選擇檔案')
textpath.grid(row=3)

addbtn = tk.Button(window, text="確認",command=lambda: check_and_run()) #,padx=5, pady=5 
addbtn.grid(row=4,ipadx=36)

#open window
window.mainloop()