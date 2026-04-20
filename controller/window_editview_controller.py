import tkinter as tk

from controller.mode_mixin import ModeContrllerMixin

from service.db_add_service import DBAddService

class EditViewController(ModeContrllerMixin):
  def __init__(self, edit_view, date_model, db_model, mode_model, id, event_bus):
    self.edit_view = edit_view
    self.date_model = date_model
    self.db_model = db_model
    self.mode_model = mode_model
    self.id = id
    self.event_bus = event_bus

    #edit_viewの削除ボタンの設定
    self.edit_view.update_delete_button(lambda: self.close_and_refresh(self.edit_view))

    #edit_view用のdb_add_serviceの接続
    self.edit_view_service = DBAddService(
      self.edit_view, 
      self.date_model, 
      self.db_model, 
      self.mode_model, 
      self.id,
      self.event_bus,
      function=lambda:self.close_and_refresh(self.edit_view)
      )
    
  
  def close_and_refresh(self, view):
    view.destroy()
    self.db_model.delete_transactions_data(self.id)
    self.event_bus.emit("data_update")
