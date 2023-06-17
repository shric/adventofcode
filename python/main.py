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
        if hasattr(sol, 'count'):
            count = sol.count
        else:
            count = 1000
        func = eval(f'sol.solution{a}')
        lam = lambda: func(f"../input/{a}.txt")

        us = timeit(lam, number=count) * 1000000/count
        answer = "".join([f"{x:>8}" for x in lam()])
        print(f"Day {a:>2}: {answer} solved in {us:.3f} µs (ran {count:>5} times)")
