import tkinter as tk
from tkinter import messagebox

from view.category_view import CategoryView
from model.datemanager_model import DateManagerModel
from model.database_model import DataBaseModel
from model.modemanager_model import ModeManagerModel
from controller.mode_mixin import ModeContrllerMixin

class CategoryViewController(ModeContrllerMixin):
  def __init__(self, category_view, date_model, db_model, mode_model,):
    self.category_view = category_view #CategoryView()
    self.date_model = date_model  #DateManagerModel()
    self.db_model = db_model #DataBaseModel()
    self.mode_model = mode_model #ModeManagerModel()
    #収入、支出ボタンを押すことで内部モードの変更と選択されたモードのボタンの色を変更する
    self.setup_mode_buttons(
      self.category_view.income_or_expense_button,
      self.mode_model
    )
    #登録ボタンを押すことでcategoriesテーブルに登録
    self.category_view.category_regist.category_button.config(command=self.add_categorys)

  
  def add_categorys(self):
    #カテゴリーテーブルにセットする名前とタイプ（income or expense）を受け取る
    self.name = self.category_view.category_regist.category_textbox.get()
    if not self.name:
      messagebox.showwarning("入力エラー", "カテゴリー名が空です。入力してください。")
    self.type = self.mode_model.get_category_mode()
    #モデルに渡して登録
    self.db_model.insert_category(self.name, self.type)
    #Viewのテキストボックスをクリアする
    self.category_view.category_regist.category_textbox.delete(0, tk.END)
