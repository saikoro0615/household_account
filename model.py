import sqlite3

class Model:
  def __init__(self, db_name="household.db"):
    #データベース作成
    self.conn = sqlite3.connect(db_name)
    self.cursor = self.conn.cursor()
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
    #データベースのコミットと接続終了
    self.conn.commit()
    self.conn.close()

if __name__ == "__main__":
  model = Model()