from controller.inputview_controller import InputViewController
from controller.confview_controller import ConfViewController
from controller.categoryview_controller import CategoryViewController
from view.main_view import MainView
from model.datemanager_model import DateManagerModel
from model.database_model import DataBaseModel
from model.modemanager_model import ModeManagerModel

class Debug():
  def __init__(self):
    # View生成
    buttons = [
      ("１：書き込み", self.go_input),
      ("２：カレンダー", self.go_conf),
      ("３：カテゴリー", self.go_category)
    ]
    self.view = MainView(buttons)
    self.date_model = DateManagerModel()
    self.db_model = DataBaseModel()
    self.mode_model = ModeManagerModel()

    # Controller接続
    self.input_controller = InputViewController(
      self.view.frames["input"],
      self.date_model,
      self.db_model,
      self.mode_model
    )
    self.conf_controller = ConfViewController(
      self.view.frames["conf"],
      self.date_model,
      self.db_model
    )

    self.category_controller = CategoryViewController(
      self.view.frames["category"],
      self.date_model,
      self.db_model,
      self.mode_model
    )


  def run(self):
    self.view.protocol("WM_DELETE_WINDOW", self.db_close)
    self.view.mainloop()

  def go_input(self):
    self.view.show_frame("input")
  def go_conf(self):
    self.view.show_frame("conf")
  def go_category(self):
    self.view.show_frame("category")

  def db_close(self):
    self.db_model.conn.close()
    self.view.destroy()

if __name__ == "__main__":
  app = Debug()
  print("デバッグ開始")
  app.run()
  print("デバッグ終了")
