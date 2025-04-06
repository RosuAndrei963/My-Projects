def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    limit = int(num ** 0.5) + 1  
    for i in range(3, limit, 2): 
        if num % i == 0:
            return False
    return True
is_prime(1234567)