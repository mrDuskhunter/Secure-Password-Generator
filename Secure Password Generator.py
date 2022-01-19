import random
import sys

DIGITS = "0123456789"
LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^_"

while True:
    pas_count = input("Количество паролей? [1-10]")
    if pas_count.isdigit() == False or 1<int(pas_count)>10:
        print("Введено неверное значение. Попробуйте снова")
        continue 
    len_pass = input("Длинна пароля? [1-20]")
    if len_pass.isdigit() == False or 1<int(len_pass)>20:
        print("Введено неверное значение. Попробуйте снова")
        continue
    else:
        break

is_numbers = input('Включать ли цифры? [y/n] ').lower() == 'y'
is_upper = input('Включать ли прописные буквы? [y/n] ').lower() == 'y'
is_lower = input('Включать ли строчные буквы? [y/n] ').lower() == 'y'
is_simb = input('Включать ли символы? [y/n] ').lower() == 'y'
#is_special = input('Исключать ли неоднозначные символы? [y/n] ').lower() == 'y'

def gen_symbols_list(is_numbers, is_upper, is_lower, is_simb):
    
    if "True" not in [str(is_numbers),str(is_upper), str(is_lower), str(is_simb)]:
        print("QWERTY123")
        sys.exit()
    
    symbols = []

    if is_numbers:
        symbols.extend(DIGITS)

    if is_upper:
        symbols.extend(UPPERCASE_LETTERS)

    if is_lower:
        symbols.extend(LOWER_LETTERS)

    if is_simb:
        symbols.extend(PUNCTUATION)

    #if is_special:
        
    return symbols


chars = gen_symbols_list(is_numbers, is_upper, is_lower, is_simb)


def generate_password(len_pass, chars):
    return [random.choice(chars) for _ in range(int(len_pass))]

for _ in range(int(pas_count)):
    print(*generate_password(len_pass, chars),sep="")