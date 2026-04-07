import tkinter as tk
import calendar

class CalendarView(tk.Frame):
  """収支を日付ごとに表示するカレンダー用クラス"""
  def __init__(self, master, year, month, data):
    super().__init__(master)
    self.year = year
    self.month = month
    self.data = data
    self.create_wigets()

  def create_wigets(self):
    #カレンダーを週ごとのリストで返す
    cal = calendar.monthcalendar(self.year, self.month)
    #グリッドをカレンダーのサイズに合わせる
    for i in range(7):
      self.grid_columnconfigure(i, weight=3)
    for i in range(len(cal)+1):
      self.grid_rowconfigure(i, weight=3)
    
    #曜日表示
    days = ["日", "月", "火", "水", "木", "金", "土"]
    for i, d in enumerate(days):
      tk.Label(self, text=d, borderwidth=1, relief="solid").grid(row=0, column=i, sticky="nsew")
    
  #カレンダー作成
    for r, week in enumerate(cal, start=1):
      for c, day in enumerate(week):
        frame = tk.Frame(self, borderwidth=1, relief="solid")
        frame.grid(row=r, column=c,sticky="nsew")
        #day=0の時、次の処理へ
        if day == 0:
          continue
        #日付を2文字として保存
        day_str = f"{day:02d}"
        #日付ラベル作成
        tk.Label(frame, text=str(day), anchor="nw").pack(anchor="nw")
        #データに金額がある場合表示
        if day_str in self.data:
          for type, amount in self.data[day_str].items():
            #typeがincomeならプラスを、そうじゃない場合は-を前につける
            text = f"+{amount}" if type == "income" else f"-{amount}"
            #incomeの場合青、そうじゃない場合は赤に色分け
            color: str = "blue" if type == "income" else "red"
            
            tk.Label(frame, text=text, fg=color, anchor="w").pack(anchor="w")