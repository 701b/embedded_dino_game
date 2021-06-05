import array
import fcntl

SSD1306_I2C_DEV = 0x3C
S_WIDTH = 128
S_HEIGHT = 64
S_PAGES = int(S_HEIGHT / 8)

i2c_fd = open('/dev/i2c-1', 'wb', buffering=0)
gpio_fd = open('/dev/rpikey', 'w')


def command_ssd1306(cmd: int) -> None:
    global i2c_fd
    
    buffer = bytes([(0 << 7) | (0 << 6), cmd])
    
    i2c_fd.write(buffer)


def init_ssd1306() -> None:
    global i2c_fd
    
    if fcntl.ioctl(i2c_fd, 0x0703, SSD1306_I2C_DEV) < 0:
        raise Exception('err setting i2c slave address')
    
    command_ssd1306(0xA8)
    command_ssd1306(0x3F)
    
    command_ssd1306(0xD3)
    command_ssd1306(0x00)
    
    command_ssd1306(0x40)
    
    command_ssd1306(0xA0)
    
    command_ssd1306(0xC0)
    
    command_ssd1306(0xDA)
    command_ssd1306(0x12)
    
    command_ssd1306(0x81)
    command_ssd1306(0x7F)
    
    command_ssd1306(0xA4)
    
    command_ssd1306(0xA6)
    
    command_ssd1306(0xD5)
    command_ssd1306(0x80)
    
    command_ssd1306(0x8D)
    command_ssd1306(0x14)
    
    command_ssd1306(0xAF)


def send_data_to_ssd1306(data: list) -> None:
    global i2c_fd
    
    buffer = bytes([(0 << 7) | (1 << 6)] + data)
    
    i2c_fd.write(buffer)


def update_ssd1306(data_to_display: list, start_x: int = 0, start_y: int = 0, end_x: int = S_WIDTH - 1, end_y: int = S_PAGES - 1) -> None:
    """
    Update data of GDDRAM
    
    Args:
        data_to_display: List consisting of 1 byte data to be displayed on the screen
        start_x: Start column
        start_y: Start page
        end_x: End column
        end_y: Start page
    """
    if len(data_to_display) != (end_x - start_x) * (end_y - start_y):
        raise Exception('Data size and length do not match.')
    
    command_ssd1306(0x20)
    command_ssd1306(0x0)
    
    command_ssd1306(0x21)
    command_ssd1306(start_x)
    command_ssd1306(start_x + end_x)
    
    command_ssd1306(0x22)
    command_ssd1306(start_y)
    command_ssd1306(start_y + end_y)
    
    send_data_to_ssd1306(data_to_display)


def get_btn_input(btn_gpio_num: int) -> bool:
    """
    Get the button's input
    
    Args:
        btn_gpio_num: GPIO number of button input to get

    Returns:
        if button is pressed, return true else false
    """
    if btn_gpio_num != 20 and btn_gpio_num != 21:
        raise Exception('The button GPIO number can only be 20 or 21.')
    
    ar = array.array('l', [2])
    
    if btn_gpio_num == 20:
        fcntl.ioctl(gpio_fd, 100, ar, True)
    elif btn_gpio_num == 21:
        fcntl.ioctl(gpio_fd, 101, ar, True)
    
    if ar[0] == 0:
        return True
    elif ar[0] == 1:
        return False
    else:
        raise Exception(f'The result of ioctl() is incorrect: {ar[0]}')


init_ssd1306()
