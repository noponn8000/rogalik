#/usr/bin/env python3
from typing import Tuple;

def hex_to_tuple(value: str) -> Tuple[int, int, int]:
   red = int(hex[0:2], 16);
   blue = int(hex[2:4], 16);
   green = int(hex[4:6], 16);

   return (red, green, blue)
