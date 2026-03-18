import tkinter as tk

class AmountView(tk.Frame):
  def __init__(self,master):
    super().__init__(master)

    #1行6列のグリッド作成
    for i in range(1):#1行
      self.grid_rowconfigure(i, weight=1)
    for i in range(6):#6列
      self.grid_columnconfigure(i, weight=1)
    
    #ラベル
    amount_label = tk.Label(self, text="金額", font=("Arial", 20),bd=2, relief="solid")
    amount_label.grid(row=0, column=0, sticky="nsew")

    #テキストボックス
    amount_text = tk.Entry(self)
    amount_text.grid(columnspan=5, row=0, column=1, padx=10,pady=10,sticky="nsew")