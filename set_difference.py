from primes_and_squares import primes_generator,squares_generator
even = set(range(0,50,2))
odd = set(range(1,50,2))

print(even)
print(odd)

prime = set(primes_generator(50))
print(prime)
square = set(squares_generator(50))
print(square)

print(odd.difference(prime))
print(odd-prime)
