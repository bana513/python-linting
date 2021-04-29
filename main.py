from __future__ import absolute_import

from typing import List, Optional, Tuple, Union

import numpy as np


def f(x, y=None):
    ...


def g(x: int, y: Optional[int] = None) -> int:
    return 2


Vector = List[float]


def func() -> Vector:
    return [1, 2, 3]


def h(x: Union[bool, List[str]]) -> Tuple[str, int]:
    return "asd", 5


def bad_type(x: int):
    ...


bad_type("asd")  # type: ignore

if __name__ == "__main__":
    print("asd", "asd")

    # fmt: off
    a = np.array([
        [1, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, -1],
    ])
    # fmt: on

    x = 5 + 2

    if x is None:
        print("asd")

    # Long line
    print(
        "asdasdasgdiausgduiasgduiasgdyas giudg aiusdg "
        + "iausgd iuags diupags dipuag duiag sdiupags dasuigd "
    )
