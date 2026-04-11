import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PieChart(tk.Frame):
  """amountsとcategoriesを受け取って円グラフにするクラス"""
  def __init__(self, master, amounts, categories):
    super().__init__(master)
    self.amounts = amounts
    self.categories = categories
    
    #フォントの指定（日本語が使えないフォントの場合文字化けするため）
    plt.rcParams["font.family"] = "MS Gothic"

    #合計
    total = sum(self.amounts)

    #円グラフを作成
    self.fig = plt.figure()
    self.ax = self.fig.add_subplot()
    
    #データがあった場合、それを用いてグラフ作成
    if total:
      self.ax.pie(self.amounts, labels=self.categories, autopct=lambda p:f"{p:.1f}%\n({int(p*total/100)}円)", startangle=90)

      #グラフの余白の調整
      self.fig.tight_layout()
    #ない場合データなしと表示
    else:
      self.ax.pie([1],labels=["データなし"],startangle=90)


    #作成した円グラフをtkinterに埋め込む
    canvas = FigureCanvasTkAgg(self.fig, master=self)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky="nsew")