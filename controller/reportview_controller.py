import tkinter as tk

class ReportViewController(tk.Frame):
  def __init__(self, report_view, date_model):
    self.report_view = report_view
    self.date_model = date_model
    self.bind_events()
    self.display_month()
   
    #ボタンにコマンドをセットする
  def bind_events(self):
    self.report_view.monthView_label.add_day_button.config(
      command=self.add_month
    )
    self.report_view.monthView_label.sub_day_button.config(
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
    self.report_view.monthView_label.dateView_label.config(
      text=self.date_model.get_month()
    )