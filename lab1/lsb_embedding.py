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

def posterization(input_path: str, secret_img: str, output_path: str) -> None:
    in_img: Image.Image
    with Image.open(input_path) as in_img:
        in_img = in_img.convert('RGB')
        in_stream: RGBStream = cast(RGBStream, in_img.get_flattened_data())
        size: tuple[int, int] = in_img.size
    with Image.open(secret_img) as in_img2:
        in_img2 = in_img2.convert('1')
        bits = [1 if pixel else 0 for pixel in in_img2.get_flattened_data()]

    aux_stream: list[RGBTuple] = []
    out_stream: list[RGBTuple] = []
    red: int
    green: int
    blue: int

    for (red, green, blue) in in_stream:
        aux_stream.append((red, (green & 254), blue))
    for (red, green, blue), bit in zip(aux_stream, bits):
        out_stream.append((red, green | bit, blue))

    out_img: Image.Image = Image.new('RGB', size)
    out_img.putdata(out_stream)
    out_img.save(output_path)
  
if __name__ == '__main__':
    posterization('images/snake.png', 'images/one_bit_image.png', 'images/lsb_embedding_output.png')
    print('Done!')