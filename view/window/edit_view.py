import tkinter as tk

from view.components.income_or_expense import IncomeOrExpense
from view.components.datetime_view import DateTimeView
from view.components.memo_view import MemoView
from view.components.amount_view import AmountView
from view.components.categorybox_view import CategoryBoxView

class EditView(tk.Toplevel):
  def __init__(self, master):
    super().__init__(master)
    self.geometry("600x600")
    self.transient(master)
    self.grab_set()
    
    #グリッド設計（4列8行）
    for i in range(4):  #4列
      self.grid_columnconfigure(i, weight=1)
    for i in range(9):  #9行
      self.grid_rowconfigure(i, weight=1)

    #収入, 支出ボタン
    self.income_or_expense_button = IncomeOrExpense(self)
    self.income_or_expense_button.grid(columnspan=2,row=0, column=1,padx=10,pady=10,sticky="nsew")
    #日付表示クラス
    self.dateView_label = DateTimeView(self)
    self.dateView_label.grid(columnspan=2,row=1, column=1, padx=10,pady=10,sticky="nsew")
    #メモ記入ボックス
    self.memo_textbox = MemoView(self)
    self.memo_textbox.grid(columnspan=2,row=2,column=1, padx=10,pady=10,sticky="nsew")
    #金額記入ボックス
    self.amount_textbox = AmountView(self)
    self.amount_textbox.grid(columnspan=2, row=3, column=1, padx=10,pady=10,sticky="nsew")
    #カテゴリリストボックス
    self.category_listbox = CategoryBoxView(self)
    self.category_listbox.grid(rowspan=3,columnspan=2,row=4,column=1,padx=10,pady=10,sticky="nsew")
    #データ登録ボタン
    self.data_regist_buttons = tk.Button(self, text="データ再登録",bg="lightblue",font=("Arial", 20),bd=2)
    self.data_regist_buttons.grid(columnspan=2,row=7,column=1,padx=10,pady=10,sticky="nsew")
    #データ削除ボタン
    self.data_delete_button = tk.Button(self, text="データ削除",bg="lightblue",font=("Arial", 20),bd=2)
    self.data_delete_button.grid(columnspan=2, row=8,column=1,padx=10,pady=10,sticky="nsew")

  def update_text(self,amount, memo):
    self.amount_textbox.set_amount(amount)
    self.memo_textbox.set_memo(memo)
