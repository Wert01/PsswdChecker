### 1. надо будет добавить для Lower 2. сделать роверку по базе простых паролей

isitgoodpsswd = 0
smalllenght = False
digit = False
upper = False

### Проверки пароля

psswd = input("Enter your password: ")
if len(psswd) >= 8 and len(psswd) < 16 :
    isitgoodpsswd += 1
    smalllenght = True
elif len(psswd) >= 16:
    isitgoodpsswd += 3

if any(char.isdigit() for char in psswd):
    isitgoodpsswd += 3
else:
    digit = True

if any(char.isupper() for char in psswd):
    isitgoodpsswd += 2
else:
    upper = True

### Выводы о пароле


if smalllenght == True:
    print("Psswd should have lenght at least 16 digit, dummy")
else:
    print("Hody partner! a lot of digits you have here! NICE!")


if digit == True:
    print("""No digits in a password? That is not even "111" type shit""")
else:
    print("digits are a good way to make your OF or PornHub account protected. Good job gooner!")

if upper == True:
    print("""it's okay just tru to use SHIFT next time""")
else:
    print("nice, you are better than a lot of people in choosing passwords")

if isitgoodpsswd == 8:
    print("ok")
elif isitgoodpsswd >= 4 and isitgoodpsswd < 8:
    print("could be better")
elif isitgoodpsswd < 4:
    print("try again!")