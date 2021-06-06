class ObjectData:
    
    def __init__(self, img_bin_data: list):
        """
        Args:
            img_bin_data: Image data represented by 1s and 0s
        """
        self.__img_bin_data = img_bin_data
        self.__x_len = len(img_bin_data[0])
        self.__y_len = len(img_bin_data)
        self.__x_pos = 0
        self.__y_pos = 0
    
    def set_pos(self, x_pos: int, y_pos: int):
        self.__x_pos = x_pos
        self.__y_pos = y_pos
    
    def get_image_data(self):
        return self.__img_bin_data, self.__x_pos, self.__y_pos, self.__x_len, self.__y_len
