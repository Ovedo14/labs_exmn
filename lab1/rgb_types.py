#----------------------------------------------------------
# Lab #1: Image Processing
#
# Date: 31-Aug-2026
# Authors:
#           A01802924 Cesar Rodriguez
#           A01803272 Oved Cornejo
#----------------------------------------------------------

from typing import Protocol

type RGBTuple = tuple[int, int, int]
type RGBStream = tuple[RGBTuple, ...]

class RGBMatrix(Protocol):
    def __getitem__(self, xy: tuple[int, int]) -> RGBTuple: ...
    def __setitem__(self, xy: tuple[int, int], value: RGBTuple) -> None: ...