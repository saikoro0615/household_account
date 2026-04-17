import tkinter as tk

class MemoView(tk.Frame):
  """メモを記入するボックス用クラス"""
  def __init__(self, master):
    super().__init__(master)

    #1行6列のグリッド作成
    for i in range(1):#1行
      self.grid_rowconfigure(i, weight=1)
    for i in range(6):#6列
      self.grid_columnconfigure(i, weight=1)

    #ラベル
    memo_label = tk.Label(self, text="メモ", font=("Arial", 20),bd=2, relief="solid")
    memo_label.grid(row=0, column=0, sticky="nsew")
    #メモ記入用のテキストボックス
    self.var = tk.StringVar()
    self.memo_text = tk.Entry(self, textvariable=self.var)
    self.memo_text.grid(columnspan=5,row=0,column=1, padx=10, sticky="nsew")
  
  def set_memo(self, memo):
    self.var.set(memo)