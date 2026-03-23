import tkinter as tk

from view.conf_view import ConfView
from model.datemanager_model import DateManagerModel
from model.database_model import DataBaseModel

class ConfViewController():
  def __init__(self, conf_view, date_model, db_model):
    self.conf_view = conf_view #ConfView()
    self.date_model = date_model #DateManagerModel()
    self.db_model = db_model #DataBaseModel()
    self.bind_events()
    self.display_month()
  #ボタンにコマンドをセットする
  def bind_events(self):
    self.conf_view.monthView_label.add_day_button.config(
      command=self.add_month
    )
    self.conf_view.monthView_label.sub_day_button.config(
      command=self.sub_month
    )
  #表示の月を1月増やす
  def add_month(self):
    self.date_model.add_month()
    self.display_month()
  #表示の月を1月減らす
  def sub_month(self):
    self.date_model.subtract_month()
    self.display_month()
  #表示を更新する
  def display_month(self):
    self.conf_view.monthView_label.dateView_label.config(
      text=self.date_model.get_month()
    )
    self.update_total_amount_label()
    self.update_month_blance_list()

  """総収入、総収支の表示"""
  def update_total_amount_label(self):
    month = self.date_model.get_month()

    #DBから取得
    income = self.db_model.get_totalamount_by_month(month,"income")
    expense = self.db_model.get_totalamount_by_month(month, "expense")
    #収支
    blance = income - expense
    #viewに反映
    self.conf_view.totalIncome_label.display_label.config(text="総収入")
    self.conf_view.totalIncome_label.incAndExp_label.config(text=f"{income}円")

    self.conf_view.totalExpense_label.display_label.config(text="総支出")
    self.conf_view.totalExpense_label.incAndExp_label.config(text=f"{expense}円")
    #もしblanceがプラスだと青、マイナスだと赤色に変更
    self.conf_view.totalIncAndExp_label.display_label.config(text="総収支")
    if blance < 0:
      color = "Red"
    else:
      color = "Blue"
    self.conf_view.totalIncAndExp_label.incAndExp_label.config(text=f"{blance}円", fg=color)

  """月間収支リストの表示"""
  def update_month_blance_list(self):
    #リスト初期化
    self.conf_view.monthIncAndExp_list.monthlist.delete(0, tk.END)
    #リストに挿入するデータを取得
    data = self.db_model.get_category_and_amount_list(self.date_model.get_month())
    #リストに挿入
    for i, (date, name, type, amount, memo) in enumerate(data):
      text = f"{date} | {name} | {memo} | {amount}円"

      self.conf_view.monthIncAndExp_list.monthlist.insert(tk.END, text)
      #typeがincomeの場合青、expenseの場合赤
      if type == "income":
        self.conf_view.monthIncAndExp_list.monthlist.itemconfig(i, fg="Blue")
      else:
        self.conf_view.monthIncAndExp_list.monthlist.itemconfig(i, fg="Red")
