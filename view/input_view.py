import tkinter as tk

from view.components.change_page_buttons import ChangePageButtons
from view.components.income_or_expense import IncomeOrExpense
from view.components.datetime_view import DateTimeView
from view.components.memo_view import MemoView
from view.components.amount_view import AmountView
from view.components.categorybox_view import CategoryBoxView


class InputView(tk.Frame):
  """収支登録用のViewクラス"""
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
    self.data_regist_buttons = tk.Button(self, text="データ登録",bg="lightblue",font=("Arial", 20),bd=2)
    self.data_regist_buttons.grid(columnspan=2,row=7,column=1,padx=10,pady=10,sticky="nsew")
