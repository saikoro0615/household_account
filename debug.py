from controller.inputview_controller import InputViewController
from controller.confview_controller import ConfViewController
from view.main_view import MainView
from model.datemanager_model import DateManagerModel
from model.database_model import DataBaseModel

class Debug():
  def __init__(self):
    # View生成
    self.view = MainView()
    self.date_model = DateManagerModel()
    self.db_model = DataBaseModel()

    # Controller接続
    self.input_controller = InputViewController(
      self.view.frames["input"],
      self.date_model,
      self.db_model
    )
    self.conf_controller = ConfViewController(
      self.view.frames["conf"],
      self.date_model,
      self.db_model
    )

  def run(self):
    self.view.mainloop()

if __name__ == "__main__":
  app = Debug()
  print("デバッグ開始")
  app.run()
  print("デバッグ終了")
