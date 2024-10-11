numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []
for number in numbers[1:]:
    for divaider in range(2, number):
        if number % divaider == 0:
            not_primes.append(number)
            break
    if number not in not_primes:
        primes.append(number)
print('not_primes:', not_primes)
print('primes:', primes)





