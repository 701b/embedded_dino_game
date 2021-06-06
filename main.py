from time import sleep

import deviceControl
from ImageProcessor import ImageProcessor
from ObjectData import ObjectData

dino_img_bin_data = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
    ]




image_processor = ImageProcessor()
dino_obj = ObjectData(dino_img_bin_data)
image_processor.add_layer(dino_obj)
image_processor.start()

for x in range(0, 128):
    dino_obj.set_pos(x, 0)
    sleep(1 / 30)
