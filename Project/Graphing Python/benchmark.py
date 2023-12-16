import os
import sys
import time

# np = sys.argv[1]
# N = sys.argv[2]

start_time = time.time()
os.system("mpirun -np 2 -hosts 172.31.41.210,172.31.36.241 ./xhpl")
end_time = time.time()

print(f"Time taken for benchmarking for N = 10,000: {end_time - start_time}s")
