import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PieChart(tk.Frame):
  """amountsとcategoriesを受け取って円グラフにするクラス"""
  def __init__(self, master, amounts, categories):
    super().__init__(master)
    self.amounts = amounts
    self.categories = categories

    #円グラフを作成
    self.fig = plt.figure()
    self.ax = self.fig.add_subplot()
    self.ax.pie(self.amounts, labels=self.categories)

    #作成した円グラフをtkinterに埋め込む
    canvas = FigureCanvasTkAgg(self.fig, master=self)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky="nsew")