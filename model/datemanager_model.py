from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

class DateManagerModel():
  def __init__(self):
    self.current_day = date.today()
    self.current_month = date.today()

  def get_day(self):
    """表示用の日付を獲得する"""
    return self.current_day

  def add_day(self):
    """表示用の日付を一日増やす"""
    self.current_day += timedelta(days=1)

  def subtract_day(self):
    """表示用の日付を一日減らす"""
    self.current_day -= timedelta(days=1)

  def get_month(self):
    """表示用の月を獲得する"""
    return self.current_month.strftime("%Y-%m")
  
  def add_month(self):
    """表示用の月を1月加算する"""
    self.current_month += relativedelta(months=1)
  
  def subtract_month(self):
    """表示用の月を1月減らす"""
    self.current_month -= relativedelta(months=1)
