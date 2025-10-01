from threading import Thread, Semaphore
from random import random
from time import sleep

semaphore = Semaphore(5)

def job():
    with semaphore:
        num_sec = random() * 5
        print(f'Processing a new job for {num_sec} seconds')
        sleep(num_sec)
        print('Job completed')

threads = []

for i in range(10):
    t = Thread(target=job)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

