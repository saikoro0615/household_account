
from datetime import date, timedelta

class Model:
  def __init__(self):
    pass






  def delete_category(self, category_id):
    """categoriesテーブルからデータを削除"""
    self._open_db()
    self.cursor.execute("""DELETE FROM categories WHERE id=?""",(category_id,))
    self._close_db()

  def delete_transactions(self, transactions_id):
    """transactionsテーブルからデータを削除"""
    self._open_db()
    self.cursor.execute("""DELETE FROM transactions WHERE id=?""",(transactions_id,))
    self._close_db()

  def print_db(self, table_name):
    """指定したテーブルの表示"""
    self._open_db()
    self.cursor.execute(f'SELECT * FROM {table_name}')
    print(self.cursor.fetchall())
    self._close_db()

  def get_db_list(self, from_date, to_date):
    """指定した範囲のデータをtransactionsテーブルから取得
    [0]:id, [1]:date, [2]:amount, [3]:category_name, [4]:category_type"""
    self._open_db()
    self.cursor.execute("""
    SELECT t.id, t.date, t.amount, c.name, c.type
    FROM transactions t
    JOIN categories c ON t.category_id = c.id
    WHERE t.date BETWEEN ? AND ?
    ORDER BY t.date
    """,
    (from_date, to_date)
    )
    get_list = self.cursor.fetchall()
    self._close_db()
    return get_list

  def total_expense_or_income_amount(self, from_date, to_date, category_type):
    """指定した範囲の総収入もしくは総支出を算出"""
    lists = self.get_db_list(from_date, to_date)
    amounts = [t[2] for t in lists]
    category_types = [t[4] for t in lists]
    total = 0
    count = 0
    for amount in amounts:
      if category_types[count] == category_type:
        total += amount
      count += 1
    return total
  
  def total_balance(self, from_date, to_date):
    """指定した範囲の総収支を算出"""
    income = self.total_expense_or_income_amount(from_date, to_date, "income")
    expense = self.total_expense_or_income_amount(from_date, to_date, "expense")
    return (income - expense)
  
  #日数に関係する関数


#デバッグ用
if __name__ == "__main__":
  model = Model()
  # today = model.current_day
  # print(today)