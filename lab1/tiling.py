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
from rgb_types import RGBMatrix


def put_images(in_grid: RGBMatrix, out_grid: RGBMatrix, width: int, height: int, offset_x: int, offset_y: int) -> None:
    for x in range(width):
        for y in range(height):
            pixel = in_grid[x,y]
            out_grid[x+offset_x,y+offset_y] = pixel

def tiling(images_paths: list[str],
           output_path: str) -> None:
    in_img: Image.Image

    with Image.open(images_paths[0]) as in_img:
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

    for i in range(len(offsets)):
        with Image.open(images_paths[i]) as in_img:
            in_img = in_img.convert('RGB')
            in_grid: RGBMatrix = cast(RGBMatrix, in_img.load())

        put_images(in_grid, out_grid, width, height, offsets[i][0], offsets[i][1])

    out_img.save(output_path)

if __name__ == '__main__':
    images_paths = ["./images/puppy.png", "./images/snake.png", "./images/tree.png","./images/woman.png"]
    output_path = "./images/tiling_output.png"
    tiling(images_paths, output_path)