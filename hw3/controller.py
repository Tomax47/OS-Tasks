#!/usr/bin/python3

import os
import sys
import signal
import subprocess

def signal_handler(signum, frame):
    print("\nSignal received, terminating...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def sanitize_expression(expression):
    valid_operators = {'+', '-', '*', '/'}

    sanitized = []
    for char in expression:
        if char.isdigit() or char in valid_operators or char.isspace():
            sanitized.append(char)

    sanitized_expression = ''.join(sanitized).strip()

    if any(op in sanitized_expression for op in valid_operators):
        return sanitized_expression
    else:
        return None

def main():
    print("Parent process (PID: {}) running".format(os.getpid()))
    print("Parent process is managing pipes")

    pipe_a_r, pipe_a_w = os.pipe()
    pipe_b_r, pipe_b_w = os.pipe()

    pid = os.fork()

    if pid == 0:
        os.close(pipe_a_r)
        os.close(pipe_b_w)

        generator_cmd = ["python3", "generator.py", "177"]
        generator_process = subprocess.Popen(generator_cmd, stdout=pipe_a_w, stderr=subprocess.PIPE)
        generator_process.wait()
        print(f"Generator process has completed.")
        os.close(pipe_a_w)
        sys.exit(0)
    else:
        os.close(pipe_a_w)
        os.close(pipe_b_r)

        while True:
            output = os.read(pipe_a_r, 1024).decode('utf-8')
            if not output:
                break

            print(f"Read from Pipe A: {output.strip()}")

            sanitized_expression = sanitize_expression(output.strip())
            if sanitized_expression:
                print(f"Processed Expression: {sanitized_expression}")
                try:
                    bc_process = subprocess.Popen(['bc'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result, _ = bc_process.communicate(input=sanitized_expression.encode())
                    print(f"Result: {result.decode('utf-8').strip()}")
                except Exception as e:
                    print(f"Error executing bc: {e}")
            else:
                print("Invalid expression, skipping...")

        os.close(pipe_a_r)
        sys.exit(0)

if __name__ == "__main__":
    main()
