import tkinter as tk

class ChangePageButtons(tk.Frame):
  """画面を切り替える用の共通ボタン用クラス"""
  def __init__(self, master, go_input, go_conf):
    super().__init__(master)

    # 2行2列のグリッドの重み付け
    self.grid_rowconfigure(0, weight=1)
    self.grid_rowconfigure(1, weight=1)
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)

    tk.Button(self, text="１：書き込み", command=go_input).grid(row=0,column=0, sticky="nsew")
    tk.Button(self, text="２：カレンダー", command=go_conf).grid(row=1, column=0, sticky="nsew")