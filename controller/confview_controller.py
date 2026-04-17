import tkinter as tk

from view.conf_view import ConfView
from view.components.calendar_view import CalendarView
from model.datemanager_model import DateManagerModel
from model.database_model import DataBaseModel

from view.window.edit_view import EditView
from controller.window_editview_controller import EditViewController

class ConfViewController():
  def __init__(self, conf_view, date_model, db_model, mode_model):
    self.conf_view = conf_view #ConfView()
    self.date_model = date_model #DateManagerModel()
    self.db_model = db_model # DataBaseModel()
    self.mode_model = mode_model #ModeManagerModel() 
    self.bind_events()
    self.display_month()
    #月間収支リストを選択したときにサブ画面を表示
    self.conf_view.monthIncAndExp_list.monthlist.bind("<<ListboxSelect>>", self.open_transactions_edit_window)

  #ボタンにコマンドをセットする
  def bind_events(self):
    self.conf_view.monthView_label.add_day_button.config(
      command=self.add_month
    )
    self.conf_view.monthView_label.sub_day_button.config(
      command=self.sub_month
    )

  #表示の月を1月増やす
  def add_month(self):
    self.date_model.add_month()
    self.display_month()

  #表示の月を1月減らす
  def sub_month(self):
    self.date_model.subtract_month()
    self.display_month()

  #表示を更新する
  def display_month(self):
    self.conf_view.monthView_label.dateView_label.config(
      text=self.date_model.get_month()
    )
    self.update_calender()
    self.update_total_amount_label()
    self.update_month_blance_list()

  """総収入、総収支の表示"""
  def update_total_amount_label(self):
    month = self.date_model.get_month()

    #DBから取得
    income = self.db_model.get_totalamount_by_month(month,"income")
    expense = self.db_model.get_totalamount_by_month(month, "expense")
    #収支
    blance = income - expense
    #viewに反映
    #総収入の更新
    self.conf_view.totalIncome_label.display_label.config(text="総収入")
    self.conf_view.totalIncome_label.incAndExp_label.config(text=f"{income}円")
    #総支出の更新
    self.conf_view.totalExpense_label.display_label.config(text="総支出")
    self.conf_view.totalExpense_label.incAndExp_label.config(text=f"{expense}円")
    #もしblanceがプラスだと青、マイナスだと赤色に変更
    self.conf_view.totalIncAndExp_label.display_label.config(text="総収支")
    if blance < 0:
      color = "Red"
    else:
      color = "Blue"
    self.conf_view.totalIncAndExp_label.incAndExp_label.config(text=f"{blance}円", fg=color)

  """月間収支リストの表示"""
  def update_month_blance_list(self):
    #リスト初期化
    self.conf_view.monthIncAndExp_list.monthlist.delete(0, tk.END)
    #内部データの初期化
    self.record_map = []
    #リストに挿入するデータを取得
    data = self.db_model.get_category_and_amount_list(self.date_model.get_month())
    #リストに挿入
    for i, (id, date, name, type, amount, memo) in enumerate(data):
      text = f"{date} | {name} | {memo} | {amount}円"
      self.conf_view.monthIncAndExp_list.monthlist.insert(tk.END, text)
      #typeがincomeの場合青、expenseの場合赤
      if type == "income":
        self.conf_view.monthIncAndExp_list.monthlist.itemconfig(i, fg="Blue")
      else:
        self.conf_view.monthIncAndExp_list.monthlist.itemconfig(i, fg="Red")
      #内部データに保存
      self.record_map.append({
        "id": id,
        "date": date,
        "name": name,
        "mtype": type,
        "amount": amount,
        "memo": memo
      })
  
  """カレンダーの表示"""
  def update_calender(self):
    month_str = self.date_model.get_month()
    #年と月に分離
    year, month = map(int, month_str.split("-"))
    #表示用のデータ
    data = self.db_model.get_calender_data(month_str)
    #カレンダーを更新
    self.conf_view.set_calendar(year, month, data)

  """データ編集用のサブ画面の表示"""
  def open_transactions_edit_window(self, event):
    #月間収支リストの選択している項目のインデックスを取得
    selection = self.conf_view.get_monthIncAndExpList_selected_index()
    #もし選択していない場合何もしない
    if not selection:
      return
    #選択している場合、その選択された項目のidを取得
    index = selection[0]
    record = self.record_map[index]

    #サブ画面の表示
    edit_view = EditView(self.conf_view)
    #サブ画面のコントローラ接続
    edit_view_controller = EditViewController(
      edit_view, 
      self.date_model, 
      self.db_model, 
      self.mode_model, 
      record["id"],
      self.display_month()
      )