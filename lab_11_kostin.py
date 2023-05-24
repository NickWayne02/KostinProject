#1
class Stack:
    def __init__(self):
        self._stack = []
        self._counter = 0

    def push(self, item):
        self._stack.append(item)
        self._counter += 1

    def pop(self):
        if self.is_empty():
            return None
        self._counter -= 1
        return self._stack.pop()

    def is_empty(self):
        return len(self._stack) == 0

    def get_counter(self):
        return self._counter

#2
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self._queue = []

    def put(self, element):
        self._queue.insert(0, element)

    def get(self):
        if self.is_empty():
            raise QueueError("Queue is empty")
        return self._queue.pop()

    def is_empty(self):
        return len(self._queue) == 0
#==================================================#
#Можна протестувати наступним кодом:
queue = Queue()
queue.put(1)
queue.put("dog")
print(queue.get())  # Виведе: 1
print(queue.get())  # Виведе: dog
print(queue.is_empty())  # Виведе: True

try:
    queue.get()
except QueueError as error:
    print("Queue error")  # Виведе: Queue error


#3
class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self._queue = []

    def put(self, element):
        self._queue.insert(0, element)

    def get(self):
        if self.isempty():
            raise QueueError("Queue is empty")
        return self._queue.pop()

    def isempty(self):
        return len(self._queue) == 0


class SuperQueue(Queue):
    def isempty(self):
        return len(self._queue) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")