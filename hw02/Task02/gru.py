#!/bin/python3

import os
import sys
import time
import random


if len(sys.argv) != 2:
    print("Usage: python gru.py <N>")
    sys.exit(1)

N = int(sys.argv[1])
if N <= 0:
    print("N must be greater than 0.")
    sys.exit(1)

child_pids = []

for _ in range(N):
    child_pid = os.fork()

    if child_pid == 0:
        random_time = random.randint(5, 10)
        os.execlp("python3", "python3", "minion.py", str(random_time))
        os._exit(1)
    else:
        print(f"Gru[{os.getpid()}]: process created. PID {child_pid}.")
        child_pids.append(child_pid)

for child_pid in child_pids:
    terminated_pid, status = os.waitpid(child_pid, 0)
    exit_status = os.WEXITSTATUS(status)
    print(f"Gru[{os.getpid()}]: process terminated. PID {terminated_pid}. Exit status {exit_status}.")

    if exit_status != 0:
        new_child_pid = os.fork()
        if new_child_pid == 0:
            random_time = random.randint(5, 10)
            os.execlp("python3", "python3", "minion.py", str(random_time))
            os._exit(1)
        else:
            print(f"Gru[{os.getpid()}]: additional process created. PID {new_child_pid}.")
