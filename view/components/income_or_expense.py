import tkinter as tk

class IncomeOrExpense(tk.Frame):
  def __init__(self, master):
    super().__init__(master)
    #1行2列のグリッド作成
    for i in range(1):
      self.grid_rowconfigure(i, weight=1)
    for i in range(2):
      self.grid_columnconfigure(i, weight=1)

    #収入ボタン
    self.income_button = tk.Button(self,text="収入",bg="lightblue", font=("Arial", 20),bd=2)
    self.income_button.grid(row=0, column=0, padx=10,pady=10,sticky="nsew")
    #支出ボタン
    self.expense_button = tk.Button(self,text="支出",bg="lightblue", font=("Arial", 20),bd=2)
    self.expense_button.grid(row=0, column=1, padx=10,pady=10,sticky="nsew")

  #モードによってボタンの色を変更
  def set_mode(self, mode):
    if mode == "income":
      self.income_button.config(bg="lightblue")
      self.expense_button.config(bg="lightgray")
    else:
      self.income_button.config(bg="lightgray")
      self.expense_button.config(bg="lightblue")

  #income,expenseボタンを押したときのコマンド設定
  def bind(self, on_income, on_expense):
    self.income_button.config(command=on_income)
    self.expense_button.config(command=on_expense)