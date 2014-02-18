class Queue(object):
  def __init__(self):
    self.queue = []

  def is_empty(self): 
    return self.size() == 0

  def size(self):
    return len(self.queue)

  def enqueue(self, item):
    self.queue.insert(0, item)

  def dequeue(self):
    if self.is_empty():
      return None
    else:
      return self.queue.pop()

  def __str__(self):
    return str(self.queue)

class QueueRear(Queue):
  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    return self.queue.pop(0)