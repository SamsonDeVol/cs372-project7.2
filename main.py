import threading
import time

ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

def sum_values(index, start, end, result):
  result[index] = sum(range(start,end+1))
  print(f"Thread: {index}, with result: {result[index]}")
    
print("Main thread starting")

# set n to length of ranges declared 
n = len(ranges)

# Create an array of `n` zeros
result = [0] * n
threads = []
# create threads of quantitiy n using runner

for i in range(n):
  t = threading.Thread(target=sum_values, args=(i,ranges[i][0],ranges[i][1],result,))
  t.start()
  threads.append(t)

for t in threads:
  t.join()

print("Main thread done")
print(f"Final results: {sum(result)}")
