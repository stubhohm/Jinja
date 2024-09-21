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
import time

start = time.time()

upper = 10000000
lower = 1
primes = [1]
prime_set = set(primes)
for i in range(lower, upper):
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

finish = time.time()
total = finish - start

#print(primes)
print(f'Total time {total}')

class Context():
    def __init__(self) -> None:
        self.upper = upper
        self.lower = lower
        
ctx = Context()

context = {
    'CTX': ctx
}

rendered_output = template.render(context)

#print(rendered_output)