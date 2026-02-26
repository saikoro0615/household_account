import sqlite3

class Model:
  def __init__(self):
    #データベース作成
    self.db_name="household.db"
    self._open_db()
    #外部キー有効化
    self.cursor.execute("PRAGMA foreign_keys= ON;")
    #categoriesテーブル作成
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      type TEXT NOT NULL CHECK(type IN ('income','expense'))
    );
    """)
    #transactionsテーブル作成
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      date TEXT NOT NULL,
      amount INTEGER NOT NULL,
      category_id INTEGER NOT NULL,
      memo TEXT,
      FOREIGN KEY (category_id) REFERENCES categories(id)
        ON DELETE CASCADE
    );
    """)
    self._close_db()

  #データベースにアクセスしてカーソルを作る関数
  def _open_db(self):
    self.conn = sqlite3.connect(self.db_name)
    self.cursor =self.conn.cursor()

  #データベースのコミットと接続終了する関数
  def _close_db(self):
    self.conn.commit()
    self.conn.close()

  #categoriesテーブルにデータを登録
  def insert_category(self, name, type):
    self._open_db()
    try:
      self.cursor.execute("""INSERT INTO categories (name, type) VALUES (?, ?)""",(name, type))
    except sqlite3.IntegrityError:
      print("typeは'income'もしくは'expense'のみです")
    self._close_db()

  #transactionsテーブルにデータを登録
  def insert_transactions(self, date, amount, category_id, memo):
    self._open_db()
    self.cursor.execute("""INSERT INTO transactions (date, amount, category_id, memo) VALUES (?, ?, ?, ?)""",(date, amount, category_id, memo))
    self._close_db()

  #categoriesテーブルからデータを削除
  def delete_category(self, category_id):
    self._open_db()
    self.cursor.execute("""DELETE FROM categories WHERE id=?""",(category_id,))
    self._close_db()

  #transactionsテーブルからデータを削除
  def delete_transactions(self, transactions_id):
    self._open_db()
    self.cursor.execute("""DELETE FROM transactions WHERE id=?""",(transactions_id,))
    self._close_db()

  #指定したテーブルの表示
  def print_db(self, table_name):
    self._open_db()
    self.cursor.execute(f'SELECT * FROM {table_name}')
    print(self.cursor.fetchall())
    self._close_db()

  #指定した範囲の総収入もしくは総支出を算出
  def total_expense_or_income_amount(self, from_date, to_date, category_type):
    self._open_db()
    self.cursor.execute("""
    SELECT t.id, t.date, t.amount, c.name
    FROM transactions t
    JOIN categories c ON t.category_id = c.id
    WHERE c.type = ?
    AND t.date BETWEEN ? AND ?
    ORDER BY t.date
    """,
    (category_type, from_date, to_date)
    )
    #リストに格納
    rows = self.cursor.fetchall()
    total = 0
    for row in rows:
      total += row[2]
    return total
  
  #指定した範囲の総収支を算出
  def total_balance(self, from_date, to_date):
    income = self.total_expense_or_income_amount(from_date, to_date, "income")
    expense = self.total_expense_or_income_amount(from_date, to_date, "expense")
    return (income - expense)



if __name__ == "__main__":
  model = Model()
  ans = model.total_balance("2026-02-01", "2026-02-28")
  print(ans)