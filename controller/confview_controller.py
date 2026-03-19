from view.conf_view import ConfView
from model.datemanager_model import DateManagerModel
from model.database_model import DataBaseModel

class ConfViewController():
  def __init__(self, conf_view, date_model, db_model):
    self.conf_view = conf_view #ConfView()
    self.date_model =date_model  #DateManagerModel()
    self.db_model = db_model #DataBaseModel()
    self.bind_events()
    self.display_month()

  def bind_events(self):
    self.conf_view.monthView_label.add_day_button.config(
      command=self.add_month
    )
    self.conf_view.monthView_label.sub_day_button.config(
      command=self.sub_month
    )
  
  def add_month(self):
    self.date_model.add_month()
    self.display_month()
  
  def sub_month(self):
    self.date_model.subtract_month()
    self.display_month()
  
  def display_month(self):
    self.conf_view.monthView_label.dateView_label.config(
      text=self.date_model.get_month()
    )
