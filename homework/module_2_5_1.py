number = int(input("Введите число: "))
for first in range(1, number):
    for second in range(first + 1, number):
        if number % (first + second) == 0:
            print(first, second, sep="", end="")
