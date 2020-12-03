#!/usr/bin/env python3


INPUT='input'


def main():
    lines = open(INPUT, 'r').readlines()
    lines = [l.split() for l in lines]
    print(lines)

    valid_passwords = 0
    valid_passwords2 = 0

    for ln in lines:
        c = ln[1][0]

        rn = ln[0].split('-')

        x = len(list(filter(lambda x: x == c, ln[2])))

        if x >= int(rn[0]) and x <= int(rn[1]):
            valid_passwords += 1

        i0, i1 = map(int, rn)
        i0 -= 1
        i1 -= 1
        try:
            if ((ln[2][i0] == c and ln[2][i1] != c) or
                    (ln[2][i0] != c and ln[2][i1] == c)):
                valid_passwords2 += 1
                print(ln)
        except Exception:
            if ln[2][i0] == c:
                valid_passwords2 += 1
                print(ln)
            continue

    print('Part1 -> ', valid_passwords)
    print('Part2 -> ', valid_passwords2)


if __name__ == '__main__':
    main()
