# -*- coding: utf-8 -*-
from pathlib import Path
import sys

### ФУНКЦИИ ПРОВЕРКИ ПАРОЛЯ ###

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
    elif len(psswd) < 11:
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
def max_repeat_run(psswd):
    if not psswd:
        return 0
    max_run = run = 1
    for i in range(1, len(psswd)):
        if psswd[i] == psswd[i-1]:
            run += 1
            max_run = max(max_run, run)
        else:
            run = 1
    return max_run



### УРОВНИ ПАРОЛЕЙ ###

def the_most_min(lv, a):
    if a == False:
        if lv.count(True) == 1:
            print("THE WORST LEVEL!")
            sys.exit(0)

# Определение минимального уровня пароля
def minscore(lv, a):
    if a == False:
        if lv.count(True) == 2:
            print("Minimal level!")
            sys.exit(0)

# Определение верхнего уровня пароля
def uppermin(lv, a):
    if a == False:
        if lv.count(True) == len(lv):
            print("Uppermin level!")
            sys.exit(0)

# Определение среднего уровня пароля
def justmid(lv, a, mxr):
    if a == False:
        if lv.count(True) >= 3 and mxr <= 2:
            print("Just mid level!")
            sys.exit(0)

# Определение хорошего уровня пароля
def good(lv, a, mxr):
    if a == True:
        if lv.count(True) == len(lv) and mxr == 1:
            print("Good level!")
            sys.exit(0)

# Определение длинного, но не сложного пароля
def dlinbad(a, lv):
    if a == True:
        if lv.count(True) < len(lv):
            print("Пароль длинный, но недостаточно сложный.")
            sys.exit(0)

# Определение длинного пароля с повторяющимися символами
def dlinpovtor(a, mxr, lv):
    if a == True:
        if mxr >= 2 and lv.count(True) == len(lv):
            print("Пароль длинный, но содержит повторяющиеся символы.")
            sys.exit(0)

# Определение длинного пароля без повторов
def good_level(a, lv, mxr):
    if a == True:
        if lv.count(True) == len(lv) and mxr == 1:
            print("Хороший уровень")
            sys.exit(0)            



def main():
    psswd = vvod()
    psswd_list(psswd)
    a = amount(psswd)
    d = digits(psswd)
    u = uppercase(psswd)
    s = special_char(psswd)
    low = lowercase(psswd)
    mxr = max_repeat_run(psswd)

    lv = [d, u, s, low]
    the_most_min(lv, a)
    minscore(lv, a)
    uppermin(lv, a)
    justmid(lv, a, mxr)
    good(lv, a, mxr)
    dlinbad(a, lv)
    dlinpovtor(a, mxr, lv)
    good_level(a, lv, mxr)

    print("Уровень пароля не определён (попробуйте изменить критерии).")



if __name__ == "__main__":
    main()

