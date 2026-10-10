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
from rgb_types import RGBTuple, RGBStream

def posterization(input_path: str, output_path: str) -> None:
    in_img: Image.Image
    with Image.open(input_path) as in_img:
        in_img = in_img.convert('RGB')
        in_stream: RGBStream = cast(RGBStream, in_img.get_flattened_data())
        size: tuple[int, int] = in_img.size
    out_stream: list[RGBTuple] = []
    for (rgb) in in_stream:
        if rgb[1] & 1 == 1:
            out_stream.append((255, 255, 255))
        else:
            out_stream.append((0, 0, 0))

    out_img: Image.Image = Image.new('RGB', size)
    out_img.putdata(out_stream)
    out_img.save(output_path)
  
if __name__ == '__main__':
    posterization('images/snake.png', 'images/lsb_extraction_output.png')
    print('Done!')