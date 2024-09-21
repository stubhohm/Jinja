from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('HelloWorld.j2')

msg = 'message'
list_items = 'list'
item_1, item_2 , item_3 = 'item 1', 'item 2', 'item 3'
bread, milk, cheese = 'bread', 'milk', 'cheese'
list_of_stuff = {item_1 : bread,
item_2 : milk,
item_3 : cheese}
upper = 1
lower = 10000

if lower > upper:
    print(f'{upper} is not lower than {lower}, idoit. Fixed it for you.')
    a = lower
    lower = upper
    upper = a

def find_primes():
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

    print(f'{len(in_range_primes)} prime numbers bettween {lower} and {upper}')
    print(f'Total time {total}')

class Context():
    def __init__(self) -> None:
        self.upper = upper
        self.lower = lower

find_primes()   

ctx = Context()

context = {
    'CTX': ctx
}

rendered_output = template.render(context)

#print(rendered_output)