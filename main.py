from model import Model
from view.main_view import MainView
from controller import Controller

def main():
  model = Model()
  view = MainView()
  controller = Controller(model, view)

if __name__ == "__main__":
  main()