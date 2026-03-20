class ModeManagerModel():
  def __init__(self):
    self.change_expense_mode()

  def get_category_mode(self):
    return self.category_mode
  
  def change_expense_mode(self):
    self.category_mode = "expense"

  def change_income_mode(self):
    self.category_mode = "income"