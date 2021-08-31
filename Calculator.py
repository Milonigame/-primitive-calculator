# калькулятор


from colorama import init

from colorama import Fore,Back,Style

init()

print(Fore.BLACK)
print(Back.CYAN)

what = input(" Что делаем?((+,-,/): ")

print(Fore.BLACK)
print(Back.YELLOW)

a =float (input (" Введите число: "))
b =float (input (" Введите число: "))



if what == "+":
    c = a + b
    print(" Результат: " + str(c))

elif what == "-":
    c = a - b
    print( " Результат: " + str(c))
elif what == "/":
    c = a / b
    print(" Результат: " + str(c))
elif what == "*":
    c = a * b
    print(" Результат: " + str(c))

else:
    print(" Неверная операция ")

inpur()


