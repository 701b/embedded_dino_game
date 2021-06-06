from time import sleep

from deviceControl import get_btn_input
from ImageProcessor import ImageProcessor
from ObjectData import ObjectData
from StringData import StringData

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

slide_dino_img_bin_data = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 1]
]

tree_img_bin_data = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
]

image_processor = ImageProcessor()
dino_obj = ObjectData(dino_img_bin_data)
image_processor.add_to_layer(dino_obj)
image_processor.start()

is_dino_stand = True

while True:
    if get_btn_input(21):
        if is_dino_stand:
            dino_obj.img_bin_data = slide_dino_img_bin_data
            dino_x_pos, dino_y_pos = dino_obj.get_pos()
            dino_obj.set_pos(dino_x_pos, dino_y_pos + 7)
            
            is_dino_stand = False
    else:
        if not is_dino_stand:
            dino_obj.img_bin_data = dino_img_bin_data
            dino_x_pos, dino_y_pos = dino_obj.get_pos()
            dino_obj.set_pos(dino_x_pos, dino_y_pos - 7)
    
            is_dino_stand = True
        
    sleep(1 / 30)
