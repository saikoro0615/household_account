import tkinter as tk
from tkinter import ttk


class ChangePageButtons(tk.Frame):
  """画面を切り替える用の共通ボタン用クラス"""
  def __init__(self, master):
    super().__init__(master)

    # 2行2列のグリッドの重み付け
    self.grid_rowconfigure(0, weight=1)
    self.grid_rowconfigure(1, weight=1)
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)

    tk.Button(self, text="１：書き込み").grid(row=0,column=0, sticky="nsew")
    tk.Button(self, text="２：カレンダー").grid(row=1, column=0, sticky="nsew")

class DateTimeView(tk.Frame):
  """日付の表示とボタンで日付のプラスマイナスをするクラス"""
  def __init__(self, master):
    super().__init__(master)

    #1行6列のグリッド作成
    for i in range(1):#1行
      self.grid_rowconfigure(i, weight=1)
    for i in range(6):#6列
      self.grid_columnconfigure(i, weight=1)

    #ラベル
    date_lebel = tk.Label(self, text="日付", font=("Arial", 20),bd=2, relief="solid")
    date_lebel.grid(row=0, column=0, sticky="nsew")

    #日付をプラスするボタン
    add_day_button = tk.Button(self, text="▶")
    add_day_button.grid(row=0, column=5, padx=10, pady=10, sticky="nsew")

    #日付をマイナスするボタン
    sub_day_button = tk.Button(self, text="◀")
    sub_day_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    #日付を表示するラベル
    dateView_label = tk.Label(self, text="test", font=("Arial", 20),bd=2, relief="solid" )
    dateView_label.grid(columnspan=3, row=0, column=2, padx=10,pady=10,sticky="nsew")

class amountView(tk.Frame):
  """金額を記入するボックス用クラス"""
  def __init__(self, master):
    super().__init__(master)

    #1行6列のグリッド作成
    for i in range(1):#1行
      self.grid_rowconfigure(i, weight=1)
    for i in range(6):#6列
      self.grid_columnconfigure(i, weight=1)
    
    #ラベル
    amount_label = tk.Label(self, text="金額", font=("Arial", 20),bd=2, relief="solid")
    amount_label.grid(row=0, column=0, sticky="nsew")

    #テキストボックス
    amount_text = tk.Entry(self)
    amount_text.grid(columnspan=5, row=0, column=1, padx=10,pady=10,sticky="nsew")

class memoView(tk.Frame):
  """メモを記入するボックス用クラス"""
  def __init__(self, master):
    super().__init__(master)

    #1行6列のグリッド作成
    for i in range(1):#1行
      self.grid_rowconfigure(i, weight=1)
    for i in range(6):#6列
      self.grid_columnconfigure(i, weight=1)

    #ラベル
    memo_label = tk.Label(self, text="メモ", font=("Arial", 20),bd=2, relief="solid")
    memo_label.grid(row=0, column=0, sticky="nsew")
    #メモ記入用のテキストボックス
    self.memo_text = tk.Entry(self)
    self.memo_text.grid(columnspan=5,row=0,column=1, padx=10,pady=10,sticky="nsew")


class CalenderView(tk.Frame):
  """収支を日付ごとに表示するカレンダー用クラス"""
  def __init__(self, master):
    super().__init__(master)

    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    #テスト用でリストで配置
    self.calender = tk.Listbox(self)
    self.calender.grid(row=0, column=0, sticky="nsew")


class IncomeAndExpenseView(tk.Frame):
  """収支を表示するラベル用クラス"""
  def __init__(self,master):
    super().__init__(master)

    #2行1列のグリッド作成
    for i in range(2):
      self.grid_rowconfigure(i, weight=0)
    for i in range(1):
      self.grid_columnconfigure(i, weight=0)
    
    #ラベル
    self.display_label = tk.Label(self, text="display", font=("Arial", 20),bd=2, relief="solid")
    self.display_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    #収支表示ラベル
    self.incAndExp_label = tk.Label(self, text="inc-or-exp",fg="Black",font=("Arial", 20),bd=2, relief="solid")
    self.incAndExp_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


class MounthIncAndExpListView(tk.Frame):
  """月間の収支を日付ごとに表示するリスト用クラス"""
  def __init__(self, master):
    super().__init__(master)

    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)

    #リストボックス（テスト用）
    self.mountlist = tk.Listbox(self)
    self.mountlist.grid(row=0, column=0, sticky="nsew")


"""View本体"""
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

    #グリッド設計（4列8行）
    for i in range(4):  #4列
      self.input_frame.grid_columnconfigure(i, weight=1)
    for i in range(8):  #8行
      self.input_frame.grid_rowconfigure(i, weight=1)
    #画面切り替え用ボタン
    ChangePageButtons(self.input_frame).grid(rowspan=2,row=0, column=0, padx=10, pady=10, sticky="nsew")
    #収入ボタン
    self.income_button = tk.Button(self.input_frame,text="収入",bg="lightblue", font=("Arial", 20),bd=2)
    self.income_button.grid(row=0, column=1, padx=10,pady=10,sticky="nsew")
    #支出ボタン
    self.expense_button = tk.Button(self.input_frame,text="支出",bg="lightblue", font=("Arial", 20),bd=2)
    self.expense_button.grid(row=0, column=2, padx=10,pady=10,sticky="nsew")
    #日付表示クラス
    self.dateView_label = DateTimeView(self.input_frame)
    self.dateView_label.grid(columnspan=2,row=1, column=1, padx=10,pady=10,sticky="nsew")
    #メモ記入ボックス
    self.memo_textbox = memoView(self.input_frame)
    self.memo_textbox.grid(columnspan=2,row=2,column=1, padx=10,pady=10,sticky="nsew")
    #金額記入ボックス
    self.amount_textbox = amountView(self.input_frame)
    self.amount_textbox.grid(columnspan=2, row=3, column=1, padx=10,pady=10,sticky="nsew")
    #カテゴリリストボックス
    self.category_listbox = tk.Listbox(self.input_frame)
    self.category_listbox.grid(rowspan=3,columnspan=2,row=4,column=1,padx=10,pady=10,sticky="nsew")
    #データ登録ボタン
    self.data_regist_buttons = tk.Button(self.input_frame, text="データ登録",bg="lightblue",font=("Arial", 20),bd=2)
    self.data_regist_buttons.grid(columnspan=2,row=7,column=1,padx=10,pady=10,sticky="nsew")

    """
    収支確認画面（conf_frame）
    """
    self.conf_frame = tk.Frame(container)
    self.conf_frame.grid(row=0, column=0, sticky="nsew")

    #グリッド設計（4列8行）
    for i in range(4):  #4列
      self.conf_frame.grid_columnconfigure(i, weight=1)
    for i in range(8):  #8行
      self.conf_frame.grid_rowconfigure(i, weight=1)
    #画面切り替えボタン
    ChangePageButtons(self.conf_frame).grid(rowspan=2,row=0, column=0, padx=10, pady=10, sticky="nsew")
    #日付表示ラベル（月）
    self.monthView_label = DateTimeView(self.conf_frame)
    self.monthView_label.grid(columnspan=3, row=0, column=1, padx=10, pady=10, sticky="nsew")
    #カレンダー
    self.calender = CalenderView(self.conf_frame)
    self.calender.grid(rowspan=3, columnspan=3, row=1, column=1, padx=10, pady=10, sticky="nsew")


    #総収入表示ラベル
    self.totalIncome_label = IncomeAndExpenseView(self.conf_frame)
    self.totalIncome_label.incAndExp_label.config(fg="Blue")
    self.totalIncome_label.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
    #総支出表示ラベル
    self.totalExpense_label = IncomeAndExpenseView(self.conf_frame)
    self.totalExpense_label.incAndExp_label.config(fg="Red")
    self.totalExpense_label.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")
    #総収支表示ラベル
    self.totalIncAndExp_label = IncomeAndExpenseView(self.conf_frame)
    self.totalIncAndExp_label.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")
    #月間収支リスト
    self.mounthIncAndExp_list = MounthIncAndExpListView(self.conf_frame)
    self.mounthIncAndExp_list.grid(rowspan=3, columnspan=3, row=5, column=1, padx=10, pady=10, sticky="nsew")

    """デバッグ用"""
    # self.input_frame.tkraise()
    self.conf_frame.tkraise()

  
if __name__ == "__main__":
  view = View()
  view.mainloop()
