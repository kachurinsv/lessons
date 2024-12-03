numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
no_primes = []

for i in range(len(numbers)):
    el = numbers[i]
    is_prime = True

    for div in range(2, el):
        if  el % div == 0:
            is_prime = False

    if is_prime:
        primes.append(el)
    else:
        no_primes.append(el)
del primes[0]
print("Простые числа: ", primes)
print("Составные числа: ", no_primes)