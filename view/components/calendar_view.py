import tkinter as tk

class CalendarView(tk.Frame):
  """収支を日付ごとに表示するカレンダー用クラス"""
  def __init__(self, master):
    super().__init__(master)

    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    #テスト用でリストで配置
    self.calendar = tk.Listbox(self)
    self.calendar.grid(row=0, column=0, sticky="nsew")