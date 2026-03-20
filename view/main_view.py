import tkinter as tk
from view.input_view import InputView
from view.conf_view import ConfView
from view.category_view import CategoryView

class MainView(tk.Tk):
  def __init__(self, buttons):
    super().__init__()

    #ウィンドウタイトル
    self.title("家計簿アプリ")
    #ウィンドウの大きさ
    self.geometry("800x600")
    #ウィンドウのグリッドを１ｘ１にする
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)
    
    #画面用のframe作成
    container = tk.Frame(self)
    container.grid(row=0, column=0, sticky="nsew")
    
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    #画面を追加
    self.frames = {}

    self.frames["input"] = InputView(container, buttons)
    self.frames["conf"] = ConfView(container, buttons)
    self.frames["category"] = CategoryView(container, buttons)

    #追加した画面を配置
    for frame in self.frames.values():
      frame.grid(row=0, column=0, sticky="nsew")
    
    #初期状態はinput画面を表示
    self.show_frame("input")
    #デバッグ用（ほかの画面を表示）
    # self.show_frame("conf")

  
  def show_frame(self, name):
    self.frames[name].tkraise()


if __name__ == "__main__":
  view = MainView()
  view.mainloop()
