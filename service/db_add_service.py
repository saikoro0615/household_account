from tkinter import messagebox
import tkinter as tk

from datetime import datetime

from controller.mode_mixin import ModeContrllerMixin


class DBAddService(ModeContrllerMixin):
  def __init__(self, view, date_model, db_model, mode_model, id=None, event_bus=None, function=None):
    self.view = view
    self.date_model = date_model
    self.db_model = db_model
    self.mode_model = mode_model
    self.event_bus = event_bus
    self.function = function
    #もしidがある場合、dbからデータを取得
    if id:
      #指定したidのデータを初期値として登録
      self.date, self.name, self.type, self.amount, self.memo = self.db_model.get_transactions_data(id)
      #str型をdatetime型に変換して設定
      self.date_model.current_day = datetime.strptime(self.date, "%Y-%m-%d").date()
      #タイプを初期値に変更
      self.mode_model.category_mode = self.type
      #ほかのテキストを更新
      self.view.update_text(self.amount, self.memo)
    
    self.bind_events()
    self.display_day()
    self.update_categorybox()
    #収入、支出ボタンを押すことで内部モードの変更と選択されたモードのボタンの色を変更する
    self.setup_mode_buttons(
      self.view.income_or_expense_button,
      self.mode_model,
      self.update_categorybox
    )
    #ボタンを押すことでtransactionsテーブルに登録
    self.view.data_regist_buttons.config(command=self.add_transactions)

  def bind_events(self):
    #日付ボタンのイベント設定
    self.view.dateView_label.add_day_button.config(
      command=self.add_day
    )
    self.view.dateView_label.sub_day_button.config(
      command=self.sub_day
    )
  
  def add_day(self):
    self.date_model.add_day()
    self.display_day()

  def sub_day(self):
    self.date_model.subtract_day()
    self.display_day()
    
  def display_day(self):
    self.view.dateView_label.dateView_label.config(
      text=self.date_model.get_day()
    )

  def update_categorybox(self):
    """カテゴリーボックスを更新する関数"""
    self.type = self.mode_model.get_category_mode()
    self.category_data = self.db_model.get_category(self.type)
    #viewに表示する用のnameを取得
    self.names = [row[1] for row in self.category_data]
    self.view.category_listbox.update_listbox(self.names)

  def add_transactions(self):
    """transactionsテーブルに登録する関数"""
    #金額の入手
    self.amount = self.view.amount_textbox.amount_text.get()
    try:
      self.amount = int(self.amount)
    except ValueError:
      messagebox.showerror("入力エラー", "金額は数字で入力してください")
      return
    #カテゴリ選択取得
    self.selection = self.view.category_listbox.category_listbox.curselection()
    if not self.selection:
      messagebox.showerror("入力エラー", "カテゴリーを選択してください")
      return
    #id取得
    index = self.selection[0]
    category_id = self.category_data[index][0]
    #日付取得
    date = self.date_model.get_day()
    #メモ取得
    memo = self.view.memo_textbox.memo_text.get()
    #モデルに渡して登録
    self.db_model.insert_transactions(date,self.amount,category_id,memo)
    #Viewのテキストボックスをクリアする
    self.view.amount_textbox.amount_text.delete(0, tk.END)
    self.view.memo_textbox.memo_text.delete(0, tk.END)
    #完了したときにメッセージボックスで知らせる
    messagebox.showinfo("登録完了","登録しました")
    #登録時にconf_viewの画面の更新
    if self.event_bus:
      self.event_bus.emit("data_update")
    #ファンクションがあるとき、それを実行
    if self.function:
      self.function()