import tkinter as tk

from view.components.change_page_buttons import ChangePageButtons

class CategoryView(tk.Frame):
  """カテゴリー登録用のViewクラス"""
  def __init__(self, master, buttons):
    super().__init__(master)

    #グリッド設計（4列8行）
    for i in range(4):  #4列
      self.grid_columnconfigure(i, weight=1)
    for i in range(8):  #8行
      self.grid_rowconfigure(i, weight=1)

    #画面切り替え用ボタン
    self.inputChangePageButtons = ChangePageButtons(self, buttons)
    self.inputChangePageButtons.grid(rowspan=2,row=0, column=0, padx=10, pady=10, sticky="nsew")