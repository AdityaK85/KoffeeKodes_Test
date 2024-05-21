def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_string(limit):
    prime_string = ""
    num = 2
    while len(prime_string) < limit:
        if is_prime(num):
            prime_string += str(num)
        num += 1
    return prime_string



def solution(n):
    prime_string = generate_prime_string(10005)
    '''
    235 71113 1719 23293137
    index = 3:3+5 = 3:8
    '''
    return prime_string[n:n+5]



print(solution(3))  # output: 71113
print(solution(0))  # output: 23571
print(solution(5))  # output: 11317