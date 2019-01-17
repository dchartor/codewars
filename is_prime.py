def is_prime(num):
    return num > 1 and not any(i % 2 == 0 for i in range(2, num))
