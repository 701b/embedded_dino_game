from threading import Thread
from time import sleep

import ObjectData
from deviceControl import *


class ImageProcessor(Thread):
    
    __FRAME_RATE = 30
    
    def __init__(self):
        super(ImageProcessor, self).__init__()
        self.__layer = []
    
    def add_to_layer(self, obj_data: ObjectData):
        self.__layer.append(obj_data)
        
    def remove_from_layer(self, obj_data: ObjectData):
        self.__layer.remove(obj_data)
        
    def __convert_to_byte_img_data(self, img_bin_data):
        result = []
        width = len(img_bin_data[0])
    
        if len(img_bin_data) % 8 != 0:
            raise Exception('The number of rows of image binary data list must be a multiple of 8.')
    
        for row_index, row in enumerate(img_bin_data):
            byte_pos = int(row_index / 8)
            byte_index = row_index % 8
            
            for col_index, value in enumerate(img_bin_data[row_index]):
                if byte_index == 0:
                    result.append(value)
                else:
                    target_index = byte_pos * width + col_index
                    result[target_index] = result[target_index] | (value << byte_index)
    
        return result
    
    def __render(self) -> list:
        rendered_frame = []
        
        for y in range(0, 64):
            row = []
        
            for x in range(0, 128):
                row.append(0)
        
            rendered_frame.append(row)
        
        for obj_data in self.__layer:
            img_byte_data, x_pos, y_pos, x_len, y_len = obj_data.get_image_data()
            
            for y_index, y in enumerate(range(y_pos, y_pos + y_len)):
                if y >= S_HEIGHT:
                    break
                    
                for x_index, x in enumerate(range(x_pos, x_pos + x_len)):
                    if x >= S_WIDTH:
                        break
                    
                    rendered_frame[y][x] = img_byte_data[y_index][x_index]
        
        return self.__convert_to_byte_img_data(rendered_frame)
    
    def run(self):
        while True:
            rendered_frame = self.__render()
            
            update_ssd1306(rendered_frame)
            
            sleep(1 / self.__FRAME_RATE)
    
    
    
    