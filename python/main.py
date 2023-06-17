#!/usr/bin/env python3

from glob import glob
from importlib import import_module
from timeit import timeit

if __name__ == "__main__":
    num = len(glob("solution*.py"))
    for i in range(num):
        a = i + 1
        module_name = f"solution{a}"
        sol = import_module(module_name)
        func = eval(f'sol.solution{a}')
        lam = lambda: func(f"../input/{a}.txt")

        us = timeit(lam, number=1000) * 1000
        print(f"Day {a}: {lam()} solved in {us:.3f} µs")
