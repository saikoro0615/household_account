import sqlite3

class DataBaseModel():
  def __init__(self):
    #データベース作成
    self.db_name="household.db"
    self.conn = sqlite3.connect(self.db_name)
    self.cursor = self.conn.cursor()
    
    self.create_tabels()


  def create_tabels(self):
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
    self.conn.commit()


  def insert_category(self, name, type):
    """categoriesテーブルにデータを登録"""
    try:
      self.cursor.execute("""INSERT INTO categories (name, type) VALUES (?, ?)""",(name, type))
      self.conn.commit()
      return True
    except sqlite3.IntegrityError:
      return False

  def get_category(self, type):
    """指定したtypeのidとnameを取得"""
    self.items = self.cursor.execute("""SELECT id, name FROM categories WHERE type=?""",(type,))
    rows = self.items.fetchall()
    return rows

  def insert_transactions(self, date, amount, category_id, memo):
    """transactionsテーブルにデータを登録"""
    try:
      self.cursor.execute("""INSERT INTO transactions (date, amount, category_id, memo) VALUES (?, ?, ?, ?)""",(date, amount, category_id, memo))
      self.conn.commit()
      return True
    except sqlite3.IntegrityError:
      return False
  
