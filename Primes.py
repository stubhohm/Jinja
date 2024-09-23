
def check_order(lower:int, upper:int):
    if lower > upper:
        print(f'{upper} is not lower than {lower}, idoit. Fixed it for you.')
        a = lower
        lower = upper
        upper = a
    return lower, upper

def find_primes(lower:int, upper:int):
    lower, upper = check_order(lower, upper)
    import time
    start = time.time()
    primes = [1]
    in_range_primes = []
    for i in range(1, upper):
        is_prime = True
        for prime_factor in primes:
            if prime_factor == 1:
                continue
            if (prime_factor * prime_factor) > i:
                break
            if (i % prime_factor) == 0:
                #print(f'{i} is not prime because it is divisible by {j}')
                is_prime = False
                break
        if is_prime and i != 1:
            primes.append(i)
        if is_prime and i >= lower:
            in_range_primes.append(i)

    finish = time.time()
    total = finish - start
    text = f'The scrip found {len(in_range_primes)} prime '
    if len(in_range_primes) > 1 or len(in_range_primes) == 0:
        text += 'numbers '
    else: 
        text += 'number '
    text += f'between the numbers {lower} and {upper}'
    return total, text
    print(f'{len(in_range_primes)} prime numbers bettween {lower} and {upper}')
    print(f'Total time {total}')