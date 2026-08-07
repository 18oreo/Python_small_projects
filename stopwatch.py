import time

input("press ENTER to start, Ctrl+c to stop.")
start = time.time()

try:
    while True:
        t = time.time() - start
        print(f"\r {int(t//3600):02d}:{int((t%3600)//60):02d}:{t%60:05.2f}", end="")
        time.sleep(0.1)
except KeyboardInterrupt:
    print(f"\n final time: {int(t//3600):02d}:{int((t%3600)//60):02d}:{t%60:05.2f} seconds")