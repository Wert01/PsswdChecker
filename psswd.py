### 1. надо будет добавить для Lower 2. сделать роверку по базе простых паролей

isitgoodpsswd = 0
smalllenght = False
digit = False
upper = False
lower = False

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
if any(char.islower() for char in psswd):
    isitgoodpsswd += 2
else:
    lower = True
if any(not char.isalnum() for char in psswd):
    isitgoodpsswd += 2
else:
    print("use different special characters in your password")

#проверка по базе простых паролей
with open("10k_most_common.txt", "r") as f:
    common_passwords = {line.strip() for line in f}

if psswd in common_passwords:
    isitgoodpsswd = 0
    print("Your password is too common! Try again.")



### Выводы о пароле

if psswd in common_passwords:
    isitgoodpsswd = 0
    print("Your password is too common! Try again.")

if smalllenght == True:
    print("Psswd should have lenght at least 16 digit, dummy")
else:
    print("Hody partner! a lot of digits you have here! NICE!")


if digit == True:
    print("""No digits in a password? That is not even "111" type shit""")
else:
    print("digits are a good way to make your OF or PornHub account protected. Good job gooner!")

if upper == True:
    print("""it's okay just try to use SHIFT next time""")
else:
    print("nice, you are better than a lot of people in choosing passwords")

if isitgoodpsswd == 8:
    print("ok")
elif isitgoodpsswd >= 4 and isitgoodpsswd < 8:
    print("could be better")
elif isitgoodpsswd < 4:
    print("try again!")

if psswd == "1111":
    print("Serious?")