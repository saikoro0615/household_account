import tkinter as tk

class CategoryLabelView(tk.Frame):
  def __init__(self, master):
    super().__init__(master)

    #2行3列のグリッド作成
    for i in range(2):#2行
      self.grid_rowconfigure(i, weight=1)
    for i in range(3):#3列
      self.grid_columnconfigure(i, weight=1)

    #カテゴリ登録用のテキストボックス
    self.category_textbox = tk.Entry(self)
    self.category_textbox.grid(columnspan=3, row=0, column=0, padx=10, pady=10, sticky="nsew")

    #カテゴリ登録ボタン
    self.category_button = tk.Button(self, text="カテゴリー登録")
    self.category_button.grid(columnspan=3, row=1, column=0, padx=10, pady=10, sticky="nsew")