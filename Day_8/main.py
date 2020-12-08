#!/usr/bin/env python3

with open('input', 'r') as fd:
    data = fd.readlines()


class Interpret:
    # SUUPORTED_INSTRUCTIONS = {
    #     'acc':
    # }

    def __init__(self, instructions):
        self.acc = 0
        self.program_counter = 0
        self.instructions = []

        self.visited_instructions = set()
        self.visited_order = []
        self.parse_instructions(instructions)
        self.proper_exit = False

    def parse_instructions(self, instructions):
        for instruction in instructions:
            instruction = instruction.strip()
            name, arg = instruction.split()

            arg = int(arg)

            if name == 'nop':
                self.instructions.append((self.pc_inc, [arg]))
            elif name == 'acc':
                self.instructions.append((self.acc_add, [arg]))
            elif name == 'jmp':
                self.instructions.append((self.jump, [arg]))
            else:
                raise Exception('Invalid instruction')

    def pc_inc(self, *args):
        self.program_counter += 1

    def acc_add(self, num, *args):
        self.acc += num
        self.program_counter += 1

    def jump(self, num, *args):
        self.program_counter += num

    def fix_cycle(self):
        for i in range(len(self.instructions)):
            if self.instructions[i][0] == self.jump:
                ins = self.instructions[i]
                self.instructions[i] = (self.pc_inc, [])
            elif self.instructions[i][0] == self.pc_inc:
                ins = self.instructions[i]
                self.instructions[i] = (self.jump, list(ins[1]))
            else:
                continue

            self.visited_order = []
            self.visited_instructions = set()
            self.acc = 0
            self.program_counter = 0

            self.run()
            if self.proper_exit:
                print('Part 2 -> ', self.acc)
                return
            else:
                self.instructions[i] = ins

    def run(self):
        while self.program_counter < len(self.instructions):
            if self.program_counter in self.visited_instructions:
                print('Part1 -> ', self.acc)
                break  # Part 1
            else:
                self.visited_instructions.add(self.program_counter)
            self.visited_order.append(self.program_counter)

            ins, args = self.instructions[self.program_counter]
            ins(*args)

        if self.program_counter == len(self.instructions):
            self.proper_exit = True


interpret = Interpret(data)
interpret.run()

interpret.fix_cycle()
