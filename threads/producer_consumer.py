import queue
from threading import Thread, Lock
from random import randint

locker = Lock()

class Producer(Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        with locker:
            for i in range(5):
                item = randint(1,100)
                self.q.put(item)
                print(f'Produced {item}')
            self.q.put(None)  # Signal the consumer to exit



class Consumer(Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        with locker:
            while True:
                item = self.q.get()
                if item is None:
                    break
                print(f'Consumed {item}')

producer = Producer(queue.Queue())
consumer = Consumer(producer.q)

producer.start()
consumer.start()

producer.join()
consumer.join()