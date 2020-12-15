#!/usr/bin/env python3

import functools


def parse_ingredient(data: str):
    d = data.strip().split(' ')
    if d[0] == 'no':
        return ('', 0)
    n = int(d[0])
    c = d[1:3]
    if not d[3].startswith('bag'):
        raise Exception('Come on')
    return (' '.join(c), n)


def bags_containing_color(data, color):
    bags = []
    for b in data.keys():
        if data[b].get(color, False):
            bags.append(b)
    return bags


with open('input', 'r') as fd:
    data = [line.strip() for line in fd]


recipes = {}


def parse_data(output, data):
    for d in data:
        product, ingredients = d.split('contain')
        product = ' '.join(product.strip().split(' ')[:2])
        if 'bag' in product:
            raise Exception('Duck')
        ings = {}
        for ing in ingredients.split(','):
            color, num = parse_ingredient(ing)
            ings[color] = num
        output[product] = ings


parse_data(recipes, data)

my_bag = 'shiny gold'
known_colors = set()
last_len = 0
colors_to_verify = [my_bag]
while True:
    new_additions = set()
    for c in colors_to_verify:
        r = bags_containing_color(recipes, c)
        new_additions.update(set(r))

    colors_to_verify = new_additions
    known_colors.update(new_additions)

    if len(known_colors) == last_len:
        break
    else:
        last_len = len(known_colors)

print('Part 1 -> ', len(known_colors))


@functools.cache
def get_inner_bags(bag_color) -> int:
    color_dict = recipes[bag_color]
    acc = 0
    for (color, count) in color_dict.items():
        if count == 0:
            return 1
        c = get_inner_bags(color)
        acc += c * count
    return acc + 1


print('Part 2 -> ', get_inner_bags(my_bag) - 1)
