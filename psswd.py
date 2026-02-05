# -*- coding: utf-8 -*-
from pathlib import Path
import sys

# Ввод пароля пользователем
def vvod():
    s = input("Vvedite parol': ")
    return s

# Проверка на наличие в списке самых распространенных паролей
def psswd_list(psswd):
    common_path = Path(__file__).with_name("most_common.txt")
    with common_path.open("r", encoding="utf-8", errors="ignore") as f:
        common_passwords = f.read().splitlines()
    if psswd in common_passwords:
        print("Слишком просто")
        sys.exit(0)
    else:
        return True
    
# Проверка длины пароля
def amount(psswd):
    if len(psswd) <= 8:
        print("Пароль слишком короткий")
        sys.exit(0)
    elif len(psswd) < 12:
        return False
    else:
        return True

# Проверка на наличие цифр в пароле
def digits(psswd):
    for char in psswd:
        if char.isdigit():
            return True
    return False

# Проверка на наличие заглавных букв в пароле
def uppercase(psswd):
    for char in psswd:
        if char.isupper():
            return True
    return False

# Проверка на наличие специальных символов в пароле
def special_char(psswd):
    for char in psswd:
        if char.isalnum() == False:
            return True
    return False

# Проверка на наличие строчных букв в пароле
def lowercase(psswd):
    for char in psswd:
        if char.islower():
            return True
    return False

# Проверка на повторяющиеся символы в пароле
def repeat(psswd):
    for i in range(len(psswd) - 1):
        if psswd[i] == psswd[i + 1]:
            return True
    return False

# Проверка на тройные повторяющиеся символы в пароле
def repeat1(psswd):
    for i in range(len(psswd) - 2):
        if psswd[i] == psswd[i + 1] == psswd[i + 2]:
            return True
    return False

# Определение минимального уровня пароля
def minscore(lv1_2, a):
    if a == False:
        if lv1_2.count(True) == 2:
            print("Minimal level!")
            sys.exit(0)

# Определение верхнего уровня пароля
def uppermin(lv1_2, a, r, r1):
    if a == False:
        if lv1_2.count(True) == len(lv1_2) and (r == True or r1 == True):
            print("Uppermin level!")
            sys.exit(0)

# Определение среднего уровня пароля
def justmid(lv3, a, r1):
    if a == False:
        if lv3.count(True) >= 3 and r1 == False:
            print("Just mid level!")
            sys.exit(0)

# Определение хорошего уровня пароля
def good(lv4, a, r1, r2):
    if a == True:
        if lv4.count(True) == len(lv4) and r1 == False and r2 == False:
            print("Good level!")
            sys.exit(0)


def main():
    psswd = vvod()
    psswd_list(psswd)
    a = amount(psswd)
    d = digits(psswd)
    u = uppercase(psswd)
    s = special_char(psswd)
    low = lowercase(psswd)
    r = repeat(psswd)
    r1 = repeat1(psswd)

    lv = [d, u, s, low]
    minscore(lv, a)
    uppermin(lv, a, r, r1)
    justmid(lv, a, r1)
    good(lv, a, r, r1)
    print("Уровень пароля не определён (попробуйте изменить критерии).")


if __name__ == "__main__":
    main()

