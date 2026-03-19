from view.input_view import InputView
from model.datemanager_model import DateManagerModel
from model.database_model import DataBaseModel


class InputViewController():
  def __init__(self,input_view):
    self.date_model = DateManagerModel()
    self.database_model = DataBaseModel()
    self.input_view = input_view
    self.bind_events()
    self.display_day()

  def bind_events(self):
    self.input_view.dateView_label.add_day_button.config(
      command=self.add_day
    )
    self.input_view.dateView_label.sub_day_button.config(
      command=self.sub_day
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
  