# Find all 2-digit prime numbers

primes = []

for num in range(10, 100):   # loop through 2-digit numbers
    is_prime = True
    for i in range(2, num):  # check divisibility
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print("2-digit prime numbers are:")
print(primes)
