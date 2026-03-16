import tkinter as tk

class ConfView(tk.Frame):
  def __init__(self, master):
    super().__init__(master)

    #グリッド設計（4列8行）
    for i in range(4):  #4列
      self.grid_columnconfigure(i, weight=1)
    for i in range(8):  #8行
      self.grid_rowconfigure(i, weight=1)