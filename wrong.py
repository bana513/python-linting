from my_lib import Object

import os

from my_lib import Object3

from my_lib import Object2

import sys

from third_party import lib15, lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8, lib9, lib10, lib11, lib12, lib13, lib14

import sys

from __future__ import absolute_import

from third_party import lib3
import numpy as np

from typing import Tuple, List, Dict, Optional, Set, Union

def f( x,y  = None):
    ...



def g(x: int, y: Optional[int] = None) -> int:
    return "asd"






Vector = List[float]

def func() -> Vector:
    return [1, 2, 3]
def h(x: Union[bool, List[str]]) -> Tuple[str, int]:
    return "asd", 5


def bad_type(x: int):
    ...

bad_type('asd') # type: ignore

if __name__ == "__main__":
    print('asd', "asd")

    # fmt: off
    a = np.array([
        [1, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, -1],
    ])
    # fmt: on

    x=5+2

    # Long line
    print('asdasdasgdiausgduiasgduiasgdyas giudg aiusdg iausgd iuags diupags dipuag duiag sdiupags dasuigd ')
