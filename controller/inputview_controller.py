from view.input_view import InputView
from model.datemanager_model import DateManagerModel
from model.database_model import DataBaseModel
from model.modemanager_model import ModeManagerModel

class InputViewController():
  def __init__(self,input_view, date_model, db_model, mode_model):
    self.input_view = input_view #InputView()
    self.date_model = date_model #DateManagerModel()
    self.database_model = db_model #DataBaseModel()
    self.mode_model = mode_model #ModeManagerModel()
    self.bind_events()
    self.display_day()

  def bind_events(self):
    #日付ボタンのイベント設定
    self.input_view.dateView_label.add_day_button.config(
      command=self.add_day
    )
    self.input_view.dateView_label.sub_day_button.config(
      command=self.sub_day
    )
    #カテゴリーボタンのイベント設定
    self.input_view.income_or_expense_button.income_button.config(
      command=self.mode_model.change_income_mode
    )
    self.input_view.income_or_expense_button.expense_button.config(
      command=self.mode_model.change_expense_mode
    )
  
  def add_day(self):
    self.date_model.add_day()
    self.display_day()

  def sub_day(self):
    self.date_model.subtract_day()
    self.display_day()
    
  def display_day(self):
    self.input_view.dateView_label.dateView_label.config(
      text=self.date_model.get_day()
    )
  