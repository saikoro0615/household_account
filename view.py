import tkinter as tk
from tkinter import ttk


#画面を切り替える用の共通ボタン用クラス
class ChangePageButtons(tk.Frame):
  def __init__(self, parent):
    super().__init__(parent)

    # 2行1列のグリッドの重み付け
    self.grid_rowconfigure(0, weight=1)
    self.grid_rowconfigure(1, weight=1)
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)

    tk.Button(self, text="１：書き込み").grid(row=0,column=0, sticky="nsew")
    tk.Button(self, text="２：カレンダー").grid(row=1, column=0, sticky="nsew")

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
    画面用のframe作成
    """
    container = tk.Frame(self)
    container.grid(row=0, column=0, sticky="nsew")
    
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    """
    収支入力画面作成(input_frame)
    """
    self.input_frame = tk.Frame(container)
    self.input_frame.grid(row=0, column=0, sticky="nsew")

    #グリッド設計（4列12行）
    for i in range(4):  #4列
      self.input_frame.grid_columnconfigure(i, weight=1)
    for i in range(8):  #12行
      self.input_frame.grid_rowconfigure(i, weight=1)
    #画面切り替え用ボタン
    ChangePageButtons(self.input_frame).grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    #収入ボタン
    self.income_button = tk.Button(self.input_frame,text="収入",bg="lightblue")
    self.income_button.grid(row=0, column=1, padx=10,pady=10,sticky="nsew")
    #支出ボタン
    self.expense_button = tk.Button(self.input_frame,text="支出",bg="lightblue")
    self.expense_button.grid(row=0, column=2, padx=10,pady=10,sticky="nsew")
    #日付表示ラベル
    self.date_label = tk.Label(self.input_frame, text="test", font=("Arial", 20),bd=2, relief="solid" )
    self.date_label.grid(columnspan=2,row=1, column=1, padx=10,pady=10,sticky="nsew")
    #メモ記入ボックス
    self.memo_text = tk.Entry(self.input_frame)
    self.memo_text.grid(columnspan=2,row=2,column=1, padx=10,pady=10,sticky="nsew")
    #金額記入ボックス
    self.amount_text = tk.Entry(self.input_frame)
    self.amount_text.grid(columnspan=2, row=3, column=1, padx=10,pady=10,sticky="nsew")
    #カテゴリリストボックス
    self.category_listbox = tk.Listbox(self.input_frame)
    self.category_listbox.grid(rowspan=3,columnspan=2,row=4,column=1,padx=10,pady=10,sticky="nsew")
    #データ登録ボタン
    self.data_regist_buttons = tk.Button(self.input_frame, text="データ登録",bg="lightblue")
    self.data_regist_buttons.grid(columnspan=2,row=7,column=1,padx=10,pady=10,sticky="nsew")

    """
    収支確認画面（conf_frame）
    """
    self.conf_frame = tk.Frame(container)
    self.conf_frame.grid(row=0, column=0, sticky="nsew")
    ChangePageButtons(self.conf_frame).grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    self.income_button = tk.Button(self.conf_frame,text="収入", bg="lightblue")
    self.income_button.grid(row=0, column=1, padx=10,pady=10,sticky="nsew")
    
    self.expense_button = tk.Button(self.conf_frame,text="支出", bg="lightblue")
    self.expense_button.grid(row=0, column=2, padx=10,pady=10,sticky="nsew")

    self.testbutton = tk.Button(self.conf_frame,text="test").grid(row=1, column=2)

    self.input_frame.tkraise()
    # self.conf_frame.tkraise()


if __name__ == "__main__":
  view = View()
  view.mainloop()
