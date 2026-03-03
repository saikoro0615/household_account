import tkinter as tk
from tkinter import ttk


#画面を切り替える用の共通ボタン用クラス
class ChangePageButtons(tk.Frame):
  def __init__(self, parent):
    super().__init__(parent)

    tk.Button(self, text="１：書き込み").pack()
    tk.Button(self, text="２：カレンダー").pack()

class View(tk.Tk):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    #ウィンドウタイトル
    self.title("家計簿アプリ")
    #ウィンドウの大きさ
    self.geometry("800x600")
    #ウィンドウのグリッドを１ｘ１にする
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)
    
    """
    収支入力画面作成(input_frame)
    """
    self.input_frame = tk.Frame(self)
    self.input_frame.grid(row=0, column=0, sticky="nsew")
    ChangePageButtons(self.input_frame).pack(anchor="nw", padx=0, pady=0)


    """
    収支確認画面（conf_frame）
    """
    self.conf_frame = tk.Frame(self)
    self.conf_frame.grid(row=0, column=0, sticky="nsew")
    ChangePageButtons(self.conf_frame).pack(anchor="nw", padx=10, pady=10)

    self.input_frame.tkraise()


if __name__ == "__main__":
  view = View()
  view.mainloop()
