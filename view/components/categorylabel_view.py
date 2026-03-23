import tkinter as tk

class CategoryLabelView(tk.Frame):
  def __init__(self, master):
    super().__init__(master)

    #3行3列のグリッド作成
    for i in range(3):#3行
      self.grid_rowconfigure(i, weight=1)
    for i in range(3):#3列
      self.grid_columnconfigure(i, weight=1)

    #カテゴリー入力催促用のラベル
    self.category_label = tk.Label(self, text="カテゴリー名を入力してください",font=("Arial", 20))
    self.category_label.grid(columnspan=3,row=0,column=0,padx=10,sticky="nsew")
    
    #カテゴリ登録用のテキストボックス
    self.category_textbox = tk.Entry(self)
    self.category_textbox.grid(columnspan=3, row=1, column=0, padx=10, pady=10, sticky="nsew")

    #カテゴリ登録ボタン
    self.category_button = tk.Button(self, text="カテゴリー登録",font=("Arial", 16))
    self.category_button.grid(columnspan=3, row=2, column=0, padx=10, pady=10, sticky="nsew")