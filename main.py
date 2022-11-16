import threading
import time

ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

def runner(index, result):
  print("new thread")
  for i in range(index):
    print(f"Thread: {i}, {0}, {1}")
    print(ranges[i])
    for j in range(ranges[i][0], ranges[i][1]+1):
      result[i] += j
    print(result)


print("Main thread starting")

# set n to length of ranges declared 
n = len(ranges)

# Create an array of `n` zeros
result = [0] * n

# create threads of quantitiy n using runner
t = threading.Thread(target=runner, args=(n,result,))
t.start()


t.join()

print(result)
print("Main thread done")