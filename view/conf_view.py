import tkinter as tk

from view.components.change_page_buttons import ChangePageButtons
from view.components.datetime_view import DateTimeView
from view.components.calendar_view import CalendarView
from view.components.income_expense_view import IncomeAndExpenseView
from view.components.month_list import MonthIncAndExpListView



class ConfView(tk.Frame):
  """収支確認用のViewクラス"""
  def __init__(self, master, buttons):
    super().__init__(master)

    #グリッド設計（4列8行）
    for i in range(4):  #4列
      self.grid_columnconfigure(i, weight=1)
    for i in range(8):  #8行
      self.grid_rowconfigure(i, weight=1)

      #画面切り替えボタン
    self.confChangePageButtons = ChangePageButtons(self, buttons)
    self.confChangePageButtons.grid(rowspan=2,row=0, column=0, padx=10, pady=10, sticky="nsew")
    #日付表示ラベル（月）
    self.monthView_label = DateTimeView(self)
    self.monthView_label.grid(columnspan=3, row=0, column=1, padx=10, pady=10, sticky="nsew")
    #カレンダー
    self.calendar = CalendarView(self)
    self.calendar.grid(rowspan=3, columnspan=3, row=1, column=1, padx=10, pady=10, sticky="nsew")


    #総収入表示ラベル
    self.totalIncome_label = IncomeAndExpenseView(self)
    self.totalIncome_label.incAndExp_label.config(fg="Blue")
    self.totalIncome_label.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
    #総支出表示ラベル
    self.totalExpense_label = IncomeAndExpenseView(self)
    self.totalExpense_label.incAndExp_label.config(fg="Red")
    self.totalExpense_label.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")
    #総収支表示ラベル
    self.totalIncAndExp_label = IncomeAndExpenseView(self)
    self.totalIncAndExp_label.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")
    #月間収支リスト
    self.mounthIncAndExp_list = MonthIncAndExpListView(self)
    self.mounthIncAndExp_list.grid(rowspan=3, columnspan=3, row=5, column=1, padx=10, pady=10, sticky="nsew")