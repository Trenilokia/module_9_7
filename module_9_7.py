def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2:
            return 'Составное'
        for i in range(2, result):
            if result % i == 0:
                return 'Составное'
        return 'Простое'
    #   
    return wrapper


@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result



result = sum_three(2, 3, 6)
print(result)
