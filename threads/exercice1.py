import os
from collections import Counter
from threading import Thread

all_files = os.listdir('.')

def treat_file(filename):
    size = os.path.getsize(filename)
    with open(filename, 'r') as f:
        content = f.read()
    all_characters = Counter(content)
    print(f"{filename} is {size} bytes.")
    print(f"Content of {filename}:", all_characters)

threads = []

for filename in all_files:
    t = Thread(target=treat_file, args=(filename,), name=f"Treating file {filename}")
    t.start()
    threads.append(t)

# Waiting for all threads to complete before ending main program 
for t in threads:
    t.join()

