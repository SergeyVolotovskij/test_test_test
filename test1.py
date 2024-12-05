# test1.py
def func(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

a: int = 10
b: int = 101.3
c: int = 200

func(a, b, c, p=4, z=6, x=50, v='HelloWord')

# args: (10, 101.3, 200)
# kwargs: {'p': 4, 'z': 6, 'x': 50, 'v': 'HelloWord'}

from typing import Union
def func2(*args, a: Union[int] = None, b: Union[int] = None):
    print(f"args: {args}")
    print(f"a / b: {a} / {b}")

func2(1,2,3,4,5,6,7, a=500, b=600)

# TODO
"""
1. Бла-бла-бла
1. Бла-бла-бла
1. Бла-бла-бла
1. Бла-бла-бла
1. Бла-бла-бла
1. Бла-бла-бла
1. Бла-бла-бла
1. Бла-бла-бла
1. Бла-бла-бла
1. Бла-бла-бла
1. Бла-бла-бла
"""