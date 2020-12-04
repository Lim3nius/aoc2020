#!/usr/bin/env python3

import re

trans_table = str.maketrans('\n', ' ')

HCL_RE = re.compile('^#[a-f0-9]{6}$')
ECL_RE = re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$')
PID_RE = re.compile('^[0-9]{9}$')


def main():
    with open('input', 'r') as fd:
        data = fd.readlines()

    # list of data dictionaries
    data = ''.join(data).split('\n\n')
    data = [d.translate(trans_table).strip() for d in data]
    data = [{kv.split(':')[0]: kv.split(':')[1] for kv in d.split(' ')} for d in data]

    valid_data = []
    for d in data:
        if len(d.keys()) == 7 and 'cid' not in d.keys():
            valid_data.append(d)
        elif len(d.keys()) == 8:
            valid_data.append(d)

    print('Part1 -> ', len(valid_data))

    valid_data2 = 0
    for d in valid_data:
        if not(1920 <= int(d['byr']) <= 2002):
            continue
        if not(2010 <= int(d['iyr']) <= 2020):
            continue
        if not(2020 <= int(d['eyr']) <= 2030):
            continue
        if not HCL_RE.match(d['hcl']):
            continue
        if not ECL_RE.match(d['ecl']):
            continue
        if not PID_RE.match(d['pid']):
            continue

        h_val = int(d['hgt'][:-2])
        if d['hgt'].endswith('cm'):
            if not (150 <= h_val <= 193):
                continue
        elif d['hgt'].endswith('in'):
            if not (59 <= h_val <= 76):
                continue
        else:
            continue

        valid_data2 += 1

    print('Part2 -> ', valid_data2)


if __name__ == '__main__':
    main()
