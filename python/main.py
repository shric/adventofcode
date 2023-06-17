#!/usr/bin/env python3

from importlib import import_module

if __name__ == "__main__":
    for i in range(2):
        a = i + 1
        print(f"Day {a}:")
        module_name = f"solution{a}"
        sol = import_module(module_name)
        eval(f'sol.solution{a}("../input/{a}.txt")')
        print()
