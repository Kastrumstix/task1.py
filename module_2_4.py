numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers)):
    for j in range(numbers[i]):
        num = numbers[i]
        is_prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3) and num !=1
    if is_prime == True:
        primes.append(numbers[i])
    if is_prime == False and numbers[i] !=1:
        not_primes.append(numbers[i])
print('Primes: ', primes)
print('Not primes ', not_primes)