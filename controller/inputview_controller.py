import tkinter as tk
from tkinter import messagebox

from view.input_view import InputView
from model.datemanager_model import DateManagerModel
from model.database_model import DataBaseModel
from model.modemanager_model import ModeManagerModel
from controller.mode_mixin import ModeContrllerMixin

from service.db_add_service import DBAddService

class InputViewController():
  def __init__(self,input_view, date_model, db_model, mode_model, event_bus):
    self.input_view = input_view #InputView() 
    self.date_model = date_model #DateManagerModel() 
    self.db_model = db_model #DataBaseModel() 
    self.mode_model = mode_model #ModeManagerModel() 
    self.event_bus = event_bus

    #input_view用のdb_add_serviceの接続
    self.input_view_service = DBAddService(
      self.input_view, 
      self.date_model, 
      self.db_model, 
      self.mode_model,
      event_bus=self.event_bus
      )