#----------------------------------------------------------
# Lab #1: Image Processing
#
# Date: 31-Aug-2026
# Authors:
#           A01802924 Cesar Rodriguez
#           A01803272 Oved Cornejo
#----------------------------------------------------------

from PIL import Image
from typing import cast
from rgb_types import RGBMatrix, RGBTuple, RGBStream

#, color1: RGBTuple, color2: RGBTuple, color3:RGBTuple

def put_images(in_grid: RGBMatrix, out_grid: RGBMatrix, width: int, height: int, offset_x: int, offset_y: int,  color1: RGBTuple, color2: RGBTuple, color3:RGBTuple) -> None:

    for x in range(width):
        for y in range(height):
            pixel = in_grid[x,y]
            r,g,b = pixel
            pixel = posterization(r,g,b,color1, color2, color3)
            out_grid[x+offset_x,y+offset_y] = pixel

def tiling(in_path: str,
           output_path: str) -> None:
    in_img: Image.Image

    with Image.open(in_path) as in_img:
        in_img = in_img.convert('RGB')
        size: tuple[int, int] = in_img.size
        in_grid: RGBMatrix = cast(RGBMatrix, in_img.load())
    x: int
    y: int
    width: int
    height: int
    width, height = size
    offsets = [(0,0), (width,0), (0,height), (width,height)]
    new_width: int = width * 2
    new_height: int = height * 2
    out_img: Image.Image = Image.new('RGB', (new_width, new_height), 'white')
    out_grid: RGBMatrix = cast(RGBMatrix, out_img.load())
    paletas = [
        ((120, 41, 15), (255, 125, 0), (255, 236, 209)),
        ((0, 0, 50), (0, 100, 200), (150, 200, 255)),
        ((50, 0, 0), (200, 50, 50), (255, 150, 150)),
        ((0, 50, 0), (50, 200, 50), (150, 255, 150))
    ]
    for i in range(len(offsets)):
        put_images(in_grid, out_grid, width, height, offsets[i][0], offsets[i][1],paletas[i][0], paletas[i][1], paletas[i][2])

    out_img.save(output_path)

def posterization(r:int, g:int,b:int, color1: RGBTuple, color2: RGBTuple, color3:RGBTuple) -> RGBTuple:
    y = (r + g + b) / 3
    if y < 50:
        nuevo_pixel = color1
    elif y >= 130:
        nuevo_pixel = color2
    else:
        nuevo_pixel = color3
    return nuevo_pixel


if __name__ == '__main__':
    image_paths = "./images/woman.png"
    output_path = "./images/ warhol_effect_output.png"
    tiling(image_paths, output_path)