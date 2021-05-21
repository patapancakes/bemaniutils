from PIL import Image  # type: ignore
from typing import Tuple

from .types.generic import Color, Matrix, Point

def affine_composite(
    img: Image.Image,
    add_color: Tuple[int, int, int, int],
    mult_color: Color,
    transform: Matrix,
    blendfunc: int,
    texture: Image.Image,
    single_threaded: bool = False,
) -> Image.Image:
    ...