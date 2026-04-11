import tkinter as tk

from view.components.change_page_buttons import ChangePageButtons
from view.components.datetime_view import DateTimeView
from view.components.pie_chart import PieChart

class ReportView(tk.Frame):
  def __init__(self, master, buttons):
    super().__init__(master)
    #グリッド設計（4列8行）
    for i in range(4):  #4列
      self.grid_columnconfigure(i, weight=1)
    for i in range(4):  #4行
      self.grid_rowconfigure(i, weight=1)

    #画面切り替え用ボタン
    self.reportChangePageButtons = ChangePageButtons(self, buttons)
    self.reportChangePageButtons.grid(rowspan=2,row=0, column=0, padx=10, pady=10, sticky="nsew")
    
    #日付表示ラベル（月）
    self.monthView_label = DateTimeView(self)
    self.monthView_label.grid(columnspan=3, row=0, column=1, padx=10, pady=10, sticky="nsew")

    #円グラフ
    self.income_piechart = None


  def set_piechart(self, amounts, categories):
    #既に設置されていた場合削除
    if self.income_piechart:
      self.income_piechart.destroy()
    #データがあった場合更新
    if amounts:
      self.amounts = amounts
      self.categories = categories
    #ない場合、0を渡す
    else:
      self.amounts = []
      self.categories = []

    self.income_piechart = PieChart(self,self.amounts, self.categories)
    self.income_piechart.grid(rowspan=3, columnspan=3, row=2, column=1, padx=10, pady=10, sticky="nsew")