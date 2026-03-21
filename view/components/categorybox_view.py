import tkinter as tk

class CategoryBoxView(tk.Frame):
  def __init__(self, master):
    super().__init__(master)

    #3行2列のグリッド作成
    for i in range(3):#3行
      self.grid_rowconfigure(i, weight=1)
    for i in range(2):#2列
      self.grid_columnconfigure(i, weight=1)

    #カテゴリリストボックス
    self.category_listbox = tk.Listbox(self, font=("Arial", 16))
    self.category_listbox.grid(rowspan=3,columnspan=2,row=0,column=0,padx=10,pady=10,sticky="nsew")
  
  def update_listbox(self, items):
    """リストボックスの中身を更新する関数"""
    self.category_listbox.delete(0, tk.END)
    for item in items:
      self.category_listbox.insert(tk.END, item)