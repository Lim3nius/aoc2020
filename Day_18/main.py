#!/usr/bin/env python3

from operator import add, mul
from functools import partial

equations = []


def parse_equation(line):
    line = line.strip()
    line = line.replace('(', '( ')
    line = line.replace(')', ' )')
    line = line.split()

    res = []
    substacks = []

    for term in line:
        if term == '(':
            substacks.append(res)
            res = []
        elif term == ')':
            tmp = substacks.pop(-1)
            tmp.append(res)
            res = tmp
        elif term in ['*', '+']:
            res.append(term)
        else:
            res.append(int(term))
    return res


def evaluate_equation(precedence, eq):
    stack = []
    for idx, term in enumerate(eq):

        if term == '+':
            stack.append(add)
        elif term == '*':
            stack.append(mul)
        elif isinstance(term, list):
            p = evaluate_equation(precedence, term)
            if precedence and idx + 1 < len(eq):
                if eq[idx+1] == '+' and eq[idx-1] == '*':
                    stack.append(p)
                    continue
            if len(stack) > 0:
                p = stack[-1](stack[-2], p)
                stack = stack[:-2]
            stack.append(p)
        elif isinstance(term, int):
            if precedence and idx + 1 < len(eq):
                if eq[idx+1] == '+' and eq[idx-1] == '*':
                    stack.append(term)
                    continue

            if len(stack) > 0 and stack[-1] in [add, mul]:
                p = stack[-1](stack[-2], term)
                stack = stack[:-2]
                stack.append(p)
            else:
                stack.append(term)
        else:
            raise Exception('Rrr')

    while len(stack) > 1:
        tmp = stack[-2](stack[-3], stack[-1])
        stack = stack[:-3]
        stack.append(tmp)

    return stack[0]


with open('input', 'r') as fd:
    for line in fd:
        equations.append(parse_equation(line))

print('Part 1 -> ', sum(map(partial(evaluate_equation, False), equations)))
print('Part 2 -> ', sum(map(partial(evaluate_equation, True), equations)))
