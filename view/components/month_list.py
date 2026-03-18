import tkinter as tk

class MonthIncAndExpListView(tk.Frame):
  """月間の収支を日付ごとに表示するリスト用クラス"""
  def __init__(self, master):
    super().__init__(master)

    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)

    #リストボックス（テスト用）
    self.mountlist = tk.Listbox(self)
    self.mountlist.grid(row=0, column=0, sticky="nsew")