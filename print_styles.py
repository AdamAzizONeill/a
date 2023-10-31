def bold(text: str) -> str:
    return '\033[1m'+ text + '\033[0m'
    
def color(
        text: str, 
        RGB: tuple = None, 
        text_color: str = None, #will only have red, green and darker green for now
        is_bold: bool = False
        ) -> str:
    
    if RGB:
        red = RGB[0]
        green = RGB[1]
        blue = RGB[2]
        text = f'\033[38;2;{str(red)};{str(green)};{str(blue)}m{text}\033[0m'
    if text_color:
        if text_color == 'green':
            text = f'\033[38;2;0;255;0m{text}\033[0m'

        if text_color == 'dark green':
            tick = u'\u2713'
            tick = bold(f'\033[38;2;0;255;0m{tick}\033[0m')
            space = '  '
            initial_space = '    '
            text =  f'\033[38;2;0;105;0m{text}\033[0m'
            text = initial_space + tick + space + text

        if text_color == 'red':
            text = f'\033[38;2;255;0;0m{text}\033[0m'

    if is_bold:
        return bold(text)
    else:
        return text