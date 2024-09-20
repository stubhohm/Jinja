from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('HelloWorld.j2')

msg = 'message'

list_items = 'list'

item_1, item_2 , item_3 = 'item 2', 'item 2', 'item 3'

bread, milk, cheese = 'bread', 'milk', 'cheese'

list_of_stuff = {item_1 : bread,
        item_2 : milk,
        item_3 : cheese}

CTX = {
    msg: 'Hello World',
    list_items : list_of_stuff
}

list_of_stuff[item_1]

rendered_output = template.render(CTX)

print(rendered_output)