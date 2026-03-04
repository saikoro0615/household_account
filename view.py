import tkinter as tk
from tkinter import ttk


#画面を切り替える用の共通ボタン用クラス
class ChangePageButtons(tk.Frame):
  def __init__(self, parent):
    super().__init__(parent)

    ttk.Button(self, text="１：書き込み").grid()
    ttk.Button(self, text="２：カレンダー").grid()

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

    #グリッド設計（3列4行）
    for i in range(3):  #3列
      self.input_frame.grid_columnconfigure(i, weight=1)
    for i in range(4):  #4行
      self.input_frame.grid_rowconfigure(i, weight=0)

    ChangePageButtons(self.input_frame).grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    self.income_button = tk.Button(self.input_frame,text="支出",width=15,height=2,bg="lightblue")
    self.income_button.grid(row=0, column=1, padx=10,pady=10, sticky="nsew")
    
    self.expense_button = tk.Button(self.input_frame,text="収入",width=15,height=2,bg="lightblue")
    self.expense_button.grid(row=0, column=2, padx=10,pady=10, sticky="nsew")


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
