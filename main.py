import time
from time import sleep
import math

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

# height : 40
aerial_obstacle_img_bin_data = [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
]

image_processor = ImageProcessor()
dino_obj = ObjectData(dino_img_bin_data)
image_processor.add_to_layer(dino_obj)

tree_obj = ObjectData(tree_img_bin_data)
image_processor.add_to_layer(tree_obj)

score_obj = StringData('SCORE:0')
image_processor.add_to_layer(score_obj)

image_processor.start()

dino_height = 14
dino_bottom = 50
dino_x = 40
dino_y = dino_bottom
current_jump_stage = 0
JUMP_STAGE = 50

tree_height = 10
tree_x = 128
tree_y = 54

while True:
    if get_btn_input(21):  # btn21 = start game
        begin = time.time()
        while True:
            if get_btn_input(20) and current_jump_stage == 0:
                current_jump_stage = JUMP_STAGE
            
            if current_jump_stage > 0:
                if current_jump_stage >= 25:
                    dino_y += 1.5 * math.cos(math.radians(180 / JUMP_STAGE * current_jump_stage))
                else:
                    dino_y += 1.5 * math.cos(math.radians(180 / JUMP_STAGE * current_jump_stage))

                current_jump_stage -= 1
            
            elif current_jump_stage == 0:
                dino_y = dino_bottom
            
            tree_x -= 1
            if tree_x <= 0:
                tree_x = 128
            
            dino_obj.set_pos(dino_x, dino_y)
            tree_obj.set_pos(tree_x, tree_y)
            sleep(1 / 30)
            
            if dino_x + 10 == tree_x:
                if dino_y <= tree_y + tree_height and dino_y >= tree_y:
                    break
            
            current = int(time.time() - begin)
            score_obj.set_string(f'SCORE:{current}')
    
    dino_height = 14
    dino_bottom = 50
    dino_x = 64
    dino_y = dino_bottom
    jump_top = 50
    current_jump_stage = 0
    
    tree_height = 10
    tree_x = 128
    tree_y = 54
    
    dino_obj.set_pos(dino_x, dino_y)
    tree_obj.set_pos(tree_x, tree_y)
