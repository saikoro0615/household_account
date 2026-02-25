import sqlite3

class Model:
  def __init__(self):
    #データベース作成
    self.db_name="household.db"
    self.open_db()
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
    self.close_db()

  #データベースにアクセスしてカーソルを作る関数
  def open_db(self):
    self.conn = sqlite3.connect(self.db_name)
    self.cursor =self.conn.cursor()

  #データベースのコミットと接続終了する関数
  def close_db(self):
    self.conn.commit()
    self.conn.close()

  #categoriesテーブルにデータを登録
  def insert_category(self, name, type):
    self.open_db()
    try:
      self.cursor.execute("""INSERT INTO categories (name, type) VALUES (?, ?)""",(name, type))
    except sqlite3.IntegrityError:
      print("typeは'income'もしくは'expense'のみです")
    self.close_db()

  #transactionsテーブルにデータを登録
  def insert_transactions(self, date, amount, category_name, category_type, memo):
    pass

  #categoriesテーブルからデータを削除
  def delete_category(self, category_id):
    self.open_db()
    self.cursor.execute("""DELETE FROM categories WHERE id=?""",(category_id,))
    self.close_db()

  #transactionsテーブルからデータを削除
  def delete_transactions(self, date, amount, category_name, category_type, memo):
    pass

  #指定したテーブルの表示
  def print_db(self, table_name):
    self.open_db()
    self.cursor.execute(f'SELECT * FROM {table_name}')
    print(self.cursor.fetchall())
    self.close_db()



if __name__ == "__main__":
  model = Model()