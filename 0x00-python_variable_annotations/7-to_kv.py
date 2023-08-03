#!/usr/bin/env python3

"""
function takes string and int
or float and returns a tuple
containing the string and the 
square of the int or float
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """returns tuple containing k and square
    of v"""
    x: Tuple[str, float] = (k, v * v)
    return x
