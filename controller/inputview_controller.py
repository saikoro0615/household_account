import tkinter as tk
from tkinter import messagebox

from view.input_view import InputView
from model.datemanager_model import DateManagerModel
from model.database_model import DataBaseModel
from model.modemanager_model import ModeManagerModel
from controller.mode_mixin import ModeContrllerMixin

class InputViewController(ModeContrllerMixin):
  def __init__(self,input_view, date_model, db_model, mode_model):
    self.input_view = input_view #InputView() 
    self.date_model = date_model #DateManagerModel() 
    self.db_model = db_model #DataBaseModel() 
    self.mode_model = mode_model #ModeManagerModel() 
    self.bind_events()
    self.display_day()
    self.update_categorybox()
    #収入、支出ボタンを押すことで内部モードの変更と選択されたモードのボタンの色を変更する
    self.setup_mode_buttons(
      self.input_view.income_or_expense_button,
      self.mode_model,
      self.update_categorybox
    )
    #ボタンを押すことでtransactionsテーブルに登録
    self.input_view.data_regist_buttons.config(command=self.add_transactions)

  def bind_events(self):
    #日付ボタンのイベント設定
    self.input_view.dateView_label.add_day_button.config(
      command=self.add_day
    )
    self.input_view.dateView_label.sub_day_button.config(
      command=self.sub_day
    )
  
  def add_day(self):
    self.date_model.add_day()
    self.display_day()

  def sub_day(self):
    self.date_model.subtract_day()
    self.display_day()
    
  def display_day(self):
    self.input_view.dateView_label.dateView_label.config(
      text=self.date_model.get_day()
    )

  def update_categorybox(self):
    """カテゴリーボックスを更新する関数"""
    self.type = self.mode_model.get_category_mode()
    self.category_data = self.db_model.get_category(self.type)
    #viewに表示する用のnameを取得
    self.names = [row[1] for row in self.category_data]
    self.input_view.category_listbox.update_listbox(self.names)

  def add_transactions(self):
    """transactionsテーブルに登録する関数"""
    #金額の入手
    self.amount = self.input_view.amount_textbox.amount_text.get()
    try:
      self.amount = int(self.amount)
    except ValueError:
      messagebox.showerror("入力エラー", "金額は数字で入力してください")
      return
    #カテゴリ選択取得
    self.selection = self.input_view.category_listbox.category_listbox.curselection()
    if not self.selection:
      messagebox.showerror("入力エラー", "カテゴリーを選択してください")
      return
    #id取得
    index = self.selection[0]
    category_id = self.category_data[index][0]
    #日付取得
    date = self.date_model.get_day()
    #メモ取得
    memo = self.input_view.memo_textbox.memo_text.get()
    #モデルに渡して登録
    self.db_model.insert_transactions(date,self.amount,category_id,memo)
    #Viewのテキストボックスをクリアする
    self.input_view.amount_textbox.amount_text.delete(0, tk.END)
    self.input_view.memo_textbox.memo_text.delete(0, tk.END)
    #完了したときにメッセージボックスで知らせる
    messagebox.showinfo("登録完了","登録しました")