import tkinter as tk

class IncomeAndExpenseView(tk.Frame):
  """収支を表示するラベル用クラス"""
  def __init__(self,master):
    super().__init__(master)

    #2行1列のグリッド作成
    for i in range(2):
      self.grid_rowconfigure(i, weight=0)
    for i in range(1):
      self.grid_columnconfigure(i, weight=0)
    
    #ラベル
    self.display_label = tk.Label(self, text="display", font=("Arial", 20),bd=2, relief="solid")
    self.display_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    #収支表示ラベル
    self.incAndExp_label = tk.Label(self, text="inc-or-exp",fg="Black",font=("Arial", 20),bd=2, relief="solid")
    self.incAndExp_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")