from datetime import date, timedelta

class DateManagerModel():
  def __init__(self):
    self.current_day = date.today()

  def get_day(self):
    """表示用の日付を獲得する"""
    return self.current_day

  def add_day(self):
    """表示用の日付を一日増やす"""
    self.current_day += timedelta(days=1)

  def subtract_day(self):
    """表示用の日付を一日減らす"""
    self.current_day -= timedelta(days=1)