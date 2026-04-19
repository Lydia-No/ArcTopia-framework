import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
from backend.core.runtime import Runtime

rt=Runtime(n=10)

start_time = time.time()
while True:
    rt.step()
    print(rt.state())
    time.sleep(0.5)
    if time.time() - start_time > 60:  # Stop after 1 minute
        break
