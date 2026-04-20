class EventBus:
  def __init__(self):
    self.listeners = {}

  def subscribe(self, event, callback):
    self.listeners.setdefault(event, []).append(callback)

  def emit(self, event, *args, **kwargs):
    for cb in self.listeners.get(event, []):
      cb(*args, **kwargs)