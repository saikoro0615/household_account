import sqlite3
import os
import sys

class DataBaseModel():
  def __init__(self):
    #データベース作成
    self.db_name= self.get_db_path()
    self.conn = sqlite3.connect(self.db_name)
    self.cursor = self.conn.cursor()
    
    self.create_tabels()


  def create_tabels(self):
    """テーブルを作成"""
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
    """指定したtypeのidとnameをcategoriesテーブルから取得"""
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
  
  def get_transactions_data(self, id):
    """transactionsテーブルから指定したidのすべてのデータを取得"""
    #テーブルから受け取るアイテムの指定
    query = """
        SELECT t.date, c.name, c.type, t.amount, t.memo
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE t.id=?
    """
    #パラメータの指定
    params = [f"{id}"]

    return self.cursor.execute(query, params).fetchone()
  
  def delete_transactions_data(self, id):
    """transactionsテーブルから指定したidのデータを削除"""
    #削除するデータの指定
    query = """
        DELETE FROM transactions WHERE id=?
    """
    #パラメータの指定
    params = [f"{id}"]
    #データ削除
    try:
      self.cursor.execute(query, params)
      self.conn.commit()
      return True
    except sqlite3.IntegrityError:
      return False
    



  def get_totalamount_by_month(self, month, type=None):
    """transactionsテーブルから指定した月とタイプのamountの合計を取得"""
    #テーブルから受け取るアイテムの指定
    query = """
        SELECT SUM(t.amount)
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE t.date LIKE ?
    """
    #パラメータの指定
    params = [f"{month}%"]
    if type in ("income", "expense"):
      query += """AND c.type = ?"""
      params.append(type)

    self.cursor.execute(query,params)
    result = self.cursor.fetchone()[0]
    return result if result is not None else 0
  
  def get_category_and_amount_list(self, month):
    """指定した月の日付とカテゴリーのnameとtype,amountとmemoを取得"""
    #テーブルから受け取るアイテムの指定
    query = """
        SELECT t.id, t.date, c.name, c.type, t.amount, t.memo
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE t.date LIKE ?
        ORDER BY t.date
    """
    #パラメータの指定
    params = [f"{month}%"]

    return self.cursor.execute(query, params).fetchall()
  
  def get_calender_data(self, month):
    """
    カレンダー表示用データを取得
    {day:[{type:total_amount},...],...}の形
    """
    #テーブルから受け取るデータの指定
    query = """
        SELECT substr(t.date, 9, 2), t.amount, c.type
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE t.date LIKE ?
        ORDER BY date
    """
    #パラメータの指定
    params = [f"{month}%"]
    rows = self.cursor.execute(query, params).fetchall()
    #同じ日付の同じタイプのamountはすべて足す
    data = {}
    for day, amount, type in rows:
      #日付がデータにない場合作成
      if day  not in data:
        data[day] = {}
      #typeがなければ作成、ある場合加算
      if type in data[day]:
        data[day][type] += amount
      else:
        data[day][type] = amount

    return data
  
  def get_piechart_data(self, month, type):
    """
    円グラフで使う用のデータを取得
    価格の多い順でソートする
    {name1:amount1,name2:amount2,...}の形
    """
    #テーブルから受け取るデータの指定
    query = """
        SELECT c.name, SUM(t.amount) as amount
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE t.date LIKE ?
        AND c.type = ?
        GROUP BY c.name
        ORDER BY amount DESC
    """
    #パラメータの指定
    params = [f"{month}%", type]
    rows = self.cursor.execute(query, params).fetchall()
    #辞書型で返す
    return {name:amount for name, amount in rows}

  def resource_path(self, relative_path):
    """exe化するにあたってのデータベースパスの指定"""
    if hasattr(sys, "_MEIPASS"):
      #exe化する場合
      base_path = sys._MEIPASS
    else:
      #通常実行の場合
      base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)
  
  def get_db_path(self):
    """exe化時に書き込み可能なDBパスを取得"""
    #exeかどうか判断
    if hasattr(sys, "_MEIPASS"):
      #ユーザー領域に保存
      app_dir = os.path.join(os.getenv("APPDATA"), "HouseholdApp")
      os.makedirs(app_dir, exist_ok=True)

      db_path = os.path.join(app_dir, "household.db")

      #初回のみコピー
      if not os.path.exists(db_path):
        init_db = self.resource_path("db/household.db")
        import shutil
        shutil.copyfile(init_db, db_path)
      return db_path
    else:
      #通常実行（exe以外の場合）
      return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "db",
        "household.db"
      )