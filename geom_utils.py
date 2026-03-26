import math
from googletrans import Translator

def calc_geometry(circle_s, square_s):
    circle_d = 2 * math.sqrt(circle_s / math.pi)
    square_a = math.sqrt(square_s)
    square_diag = square_a * math.sqrt(2)
    
    c_in_s = circle_d <= square_a
    s_in_c = square_diag <= circle_d
    
    return round(circle_d, 2), round(square_a, 2), round(square_diag, 2), c_in_s, s_in_c

def translate_text(text, lang):
    if lang == 'uk':
        return text
    try:
        translator = Translator()
        res = translator.translate(text, dest=lang)
        return res.text
    except:
        return text