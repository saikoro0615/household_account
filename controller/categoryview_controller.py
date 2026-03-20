from view.category_view import CategoryView
from model.datemanager_model import DateManagerModel
from model.database_model import DataBaseModel
from model.modemanager_model import ModeManagerModel
from controller.mode_mixin import ModeContrllerMixin

class CategoryViewController(ModeContrllerMixin):
  def __init__(self, category_view, date_model, db_model, mode_model,):
    self.category_view = category_view #CategoryView()
    self.date_model = date_model  #DateManagerModel()
    self.db_model = DataBaseModel() #db_model
    self.mode_model = mode_model #ModeManagerModel()
    
    self.setup_mode_buttons(
      self.category_view.income_or_expense_button,
      self.mode_model
    )

