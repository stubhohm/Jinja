from jinja2 import Environment, FileSystemLoader

from Primes import find_primes

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('HelloWorld.j2')

msg = 'Hello World'
list_items = 'list'
item_1, item_2 , item_3 = 'item 1', 'item 2', 'item 3'
bread, milk, cheese = 'bread', 'milk', 'cheese'
list_of_stuff = {item_1 : bread,
item_2 : milk,
item_3 : cheese}

def hello_world():
    return 'Hello World from Python'
'''
lower = 1
upper = 100
time, quant_of_primes = find_primes(lower, upper)
print(f'{quant_of_primes} prime numbers bettween {lower} and {upper}')
print(f'Total time {time}')
'''

class Context():
    def __init__(self) -> None:
        self.message = msg
        self.item_list = list_of_stuff
        self.lower = 10
        self.upper = 100
        self.find_primes = find_primes
        self.hello_world = hello_world


ctx = Context()

context = {
    'CTX': ctx
}

print('pre rendering')
rendered_output = template.render(context)
print('post rendering')
print(rendered_output)