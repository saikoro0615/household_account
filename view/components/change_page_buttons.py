import tkinter as tk

class ChangePageButtons(tk.Frame):
  """画面を切り替える用の共通ボタン用クラス"""
  def __init__(self, master, buttons):
    super().__init__(master)

    # buttonsの数だけ行を増やしてグリッドの重み付け
    for i in range(len(buttons)):
      self.grid_rowconfigure(i, weight=1)
    self.grid_columnconfigure(0, weight=1)

    #ボタンの作製
    for i, (text, command) in enumerate(buttons):
      tk.Button(self, text=text, command=command).grid(row=i,column=0, sticky="nsew")