import tkinter as tk

from controller.mode_mixin import ModeContrllerMixin

class ReportViewController(ModeContrllerMixin):
  def __init__(self, report_view, date_model, db_model, mode_model):
    self.report_view = report_view
    self.date_model = date_model
    self.db_model = db_model
    self.mode_model = mode_model
    self.bind_events()
    self.display_month()
    self.setup_mode_buttons(
      self.report_view.income_or_expense_button,
      self.mode_model,
      self.update_piechart
    )
   
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
    self.update_piechart()
  #円グラフの更新
  def update_piechart(self):
    #表示する月とタイプ
    month = self.date_model.get_month()
    type = self.mode_model.get_category_mode()
    #データを取得
    data = self.db_model.get_piechart_data(month, type)
    amounts, categories = data.values(), data.keys()
    #円グラフを更新
    self.report_view.set_piechart(amounts, categories)