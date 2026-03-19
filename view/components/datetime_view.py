import tkinter as tk

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
    self.date_lebel = tk.Label(self, text="日付", font=("Arial", 20),bd=2, relief="solid")
    self.date_lebel.grid(row=0, column=0, sticky="nsew")

    #日付をプラスするボタン
    self.add_day_button = tk.Button(self, text="▶")
    self.add_day_button.grid(row=0, column=5, padx=10, pady=10, sticky="nsew")

    #日付をマイナスするボタン
    self.sub_day_button = tk.Button(self, text="◀")
    self.sub_day_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    #日付を表示するラベル
    self.dateView_label = tk.Label(self, text="test", font=("Arial", 20),bd=2, relief="solid" )
    self.dateView_label.grid(columnspan=3, row=0, column=2, padx=10,pady=10,sticky="nsew")