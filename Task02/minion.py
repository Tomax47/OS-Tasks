#!/bin/python3

import os
import sys
import time
import random

if len(sys.argv) != 2:
    print("Usage: python minion.py <S>")
    sys.exit(1)

S = int(sys.argv[1])
print(f"Minion[{os.getpid()}]: created. Parent PID {os.getppid()}.")

time.sleep(S)

exit_status = random.randint(0, 1)
print(f"Child[{os.getpid()}]: before terminated. Parent PID {os.getppid()}. Exit status {exit_status}.")

os._exit(exit_status)
