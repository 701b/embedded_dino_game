import time
from time import sleep
import math

from deviceControl import get_btn_input
from ImageProcessor import ImageProcessor
from ObjectData import ObjectData
from StringData import StringData

DINO_HEIGHT = 14
DINO_WIDTH = 10
DINO_IMG_BIN_DATA = [
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

DINO_SLIDE_HEIGHT = 7
DINO_SLIDE_IMG_BIN_DATA = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 1]
]

TREE_HEIGHT = 10
TREE_WIDTH = 9
TREE_IMG_BIN_DATA = [
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
AERIAL_OBSTACLE_WIDTH = 8
AERIAL_OBSTACLE_IMG_BIN_DATA = [
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

DINO_BOTTOM = 50
JUMP_STAGE = 50

image_processor = ImageProcessor()
image_processor.start()

dino_obj = ObjectData(DINO_IMG_BIN_DATA)
tree_obj = ObjectData(TREE_IMG_BIN_DATA)
aerial_obstacle_obj = ObjectData(AERIAL_OBSTACLE_IMG_BIN_DATA)
score_obj = StringData('SCORE:0')

main_obj = StringData('DINO GAME')
main_obj.set_pos(32, 20)

press_any_btn_obj = StringData('PRESS ANY BUTTON')
press_any_btn_obj.set_pos(8, 35)

while True:
    image_processor.clear_layer()
    image_processor.add_to_layer(main_obj)
    image_processor.add_to_layer(press_any_btn_obj)
    image_processor.add_to_layer(score_obj)
    
    if get_btn_input(20) or get_btn_input(21):
        image_processor.clear_layer()
        image_processor.add_to_layer(score_obj)
        image_processor.add_to_layer(dino_obj)
        image_processor.add_to_layer(tree_obj)
        image_processor.add_to_layer(aerial_obstacle_obj)
        
        begin = time.time()
        
        dino_x = 20
        dino_y = DINO_BOTTOM
        current_jump_stage = 0
        
        tree_x = 128
        tree_y = 54
        
        is_dino_stand = True
        
        aerial_y = 14
        aerial_x = 180

        dino_obj.set_pos(dino_x, dino_y)
        tree_obj.set_pos(tree_x, tree_y)
        aerial_obstacle_obj.set_pos(aerial_x, aerial_y)

        score_obj.set_string(f'SCORE:0')
        
        sleep(1)
        
        while True:
            if get_btn_input(20) and current_jump_stage == 0:  # btn20 = jump
                current_jump_stage = JUMP_STAGE
            
            if get_btn_input(21) and current_jump_stage == 0:  # btn21 = slide
                if is_dino_stand:
                    dino_obj.img_bin_data = DINO_SLIDE_IMG_BIN_DATA
                    dino_y += 7
                    
                    is_dino_stand = False
            else:
                if not is_dino_stand:
                    dino_obj.img_bin_data = DINO_IMG_BIN_DATA
                    dino_y -= 7
                    
                    is_dino_stand = True
            
            if current_jump_stage > 0:
                if current_jump_stage >= 25:
                    dino_y += 1.5 * math.cos(math.radians(180 / JUMP_STAGE * current_jump_stage))
                else:
                    dino_y += 1.5 * math.cos(math.radians(180 / JUMP_STAGE * current_jump_stage))
                
                current_jump_stage -= 1
                
                if current_jump_stage == 0:
                    dino_y = DINO_BOTTOM
            
            tree_x -= 1
            if tree_x <= 0:
                tree_x = 128
            
            aerial_x -= 1
            if aerial_x <= 0:
                aerial_x = 128
            
            dino_obj.set_pos(dino_x, dino_y)
            tree_obj.set_pos(tree_x, tree_y)
            aerial_obstacle_obj.set_pos(aerial_x, aerial_y)
            
            sleep(1 / 30)
            
            if dino_x + 1 <= tree_x <= dino_x + TREE_WIDTH - 1 and dino_y + 1 <= tree_y <= dino_y + DINO_HEIGHT - 1:
                sleep(0.5)
                break
            else:
                if dino_x <= aerial_x <= dino_x + AERIAL_OBSTACLE_WIDTH and is_dino_stand:
                    sleep(0.5)
                    break
            
            current = int(time.time() - begin)
            score_obj.set_string(f'SCORE:{current}')
    
    sleep(1 / 60)
