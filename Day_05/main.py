#!/usr/bin/env python3

def decode_row(data):
    return binary(0, 127, 'F', 'B', data[:7])


def decode_column(data):
    return binary(0, 7, 'L', 'R', data[7:])


def getID(row: int, column: int) -> int:
    return 8 * row + column


# def binary_search(lth: int, hth: int, llt: str, hlt: str, data: str) -> int:
#     lower, higher = lth, hth
#     for c in data:
#         middle = (lower + higher) // 2

#         if c == llt:
#             higher = middle
#         elif c == hlt:
#             lower = middle
#         else:
#             raise Exception(f'Fucked up {c}')

#     if data[-1] == llt:
#         return lower
#     else:
#         return higher

def binary(lth: int, hth: int, llt: str, hlt: str, data: str) -> int:
    n = 0
    for c in data:
        if c == llt:
            ...
        elif c == hlt:
            n = n | 0x1
        else:
            raise Exception('Foo')

        n <<= 1

    return n >> 1


def main():
    with open('input', 'r') as fd:
        data = [line.strip() for line in fd]

    dd = []
    maxID = 0

    for d in data:
        r = decode_row(d)
        c = decode_column(d)

        i = getID(r, c)
        if i > maxID:
            maxID = i

        dd.append({'r': r, 'c': c, 'id': i, 'txt': d})

    print('Part1 -> ', maxID)

    # Part 2
    # ids = [e['id'] for e in dd]
    dd = sorted(dd, key=lambda e: e['id'])

    print(dd)
    for i in range(len(dd)-1):
        if dd[i+1]['id'] - dd[i]['id'] == 2:
            print('Part2 -> ', dd[i]['id'] + 1)


if __name__ == '__main__':
    main()
