def generate_odd_prime_numbers():
    prime_numbers = []
    for n in range(1, 3001):
        if is_prime(n):
            prime_numbers.append(n)
    return prime_numbers

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

odd_prime_numbers = generate_odd_prime_numbers()
print(odd_prime_numbers)
