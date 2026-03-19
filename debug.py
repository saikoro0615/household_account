import tkinter as tk
from controller.inputview_controller import InputViewController
from view.input_view import InputView

class Debug():
  def __init__(self):
    self.root = tk.Tk()
    self.root.geometry("800x600")

    # View生成
    self.view = InputView(self.root)
    self.view.pack(fill="both", expand=True)

    # Controller接続
    self.controller = InputViewController(self.view)

  def run(self):
    self.root.mainloop()

if __name__ == "__main__":
  app = Debug()
  print("デバッグ開始")
  app.run()
  print("デバッグ終了")
