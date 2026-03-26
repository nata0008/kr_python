import json
import os
from geom_utils import calc_geometry, translate_text

def main():
    file_name = "MyData.json"
    
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            circle_s = float(data['circle'])
            square_s = float(data['square'])
            lang = data.get('lang', 'uk')
            
            circle_d, square_a, square_diag, c_in_s, s_in_c = calc_geometry(circle_s, square_s)
            
            c_str = str(int(circle_s)) if circle_s.is_integer() else str(circle_s)
            s_str = str(int(square_s)) if square_s.is_integer() else str(square_s)
            
            print(f"{translate_text('Мова', lang)}: {translate_text('Українська', lang) if lang=='uk' else lang}")
            print(f"{translate_text('Площа кола', lang)}: {c_str}")
            print(f"{translate_text('Площа квадрата', lang)}: {s_str}")
            print(f"{translate_text('Діаметр кола', lang)}: {str(circle_d).replace('.', ',')}")
            print(f"{translate_text('Сторона квадрата', lang)}: {str(int(square_a) if square_a.is_integer() else square_a).replace('.', ',')}")
            print(f"{translate_text('Діагональ квадрата', lang)}: {str(square_diag).replace('.', ',')}\n")
            
            t_a_yes = f"а) Коло з площею {c_str} вміститься в квадраті з площею {s_str}."
            t_a_no = f"а) Коло з площею {c_str} не вміститься в квадраті з площею {s_str}."
            t_b_yes = f"б) Квадрат с площею {s_str} вміститься в колі з площею {c_str}."
            t_b_no = f"б) Квадрат с площею {s_str} не вміститься в колі з площею {c_str}."

            print(translate_text(t_a_yes, lang) if c_in_s else translate_text(t_a_no, lang))
            print(translate_text(t_b_yes, lang) if s_in_c else translate_text(t_b_no, lang))
                
            return
        except Exception:
            pass
            
    circle_s = input("Введіть площу кола: ")
    square_s = input("Введіть площу квадрата: ")
    lang = input("Введіть мову інтерфейсу: ")
    
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump({"circle": circle_s, "square": square_s, "lang": lang}, f)
        
    print(f"Дані збережено в файл {file_name}")

if __name__ == "__main__":
    main()