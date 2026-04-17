import tkinter as tk

from controller.mode_mixin import ModeContrllerMixin

from service.db_add_service import DBAddService

class EditViewController(ModeContrllerMixin):
  def __init__(self, edit_view, date_model, db_model, mode_model, id, function):
    self.edit_view = edit_view
    self.date_model = date_model
    self.db_model = db_model
    self.mode_model = mode_model
    self.id = id
    self.function = function

    #edit_view用のdb_add_serviceの接続
    self.edit_view_service = DBAddService(
      self.edit_view, 
      self.date_model, 
      self.db_model, 
      self.mode_model, 
      self.id,
      on_close=lambda: self.close_and_refresh(edit_view)
      )
    
  
  def close_and_refresh(self, view):
    view.destroy()
    self.function()
