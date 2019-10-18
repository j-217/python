# def simple_assembler(program):
#     i = 0
#     d = {}
#     while i < len(program):
#         cmd, r, v = (program[i] + ' 0').split()[:3]
#         if cmd == 'mov':
#             d[r] = d[v] if v in d else int(v)
#         if cmd == 'inc':
#             d[r] += 1
#         if cmd == 'dec':
#             d[r] -= 2
#         if cmd == 'jnz' and (d[r] if r in d else int(r)):
#             i += int(v) - 1
#         i += 1
#     print(d)
#     return d


class Interpret:

    def __init__(self):
        self.vars = {}
        self.ins = {}
        self.pc = 0
        self.ins['mov'] = self.__ins_mov
        self.ins['inc'] = self.__ins_inc
        self.ins['dec'] = self.__ins_dec
        self.ins['jnz'] = self.__ins_jnz

    def get_value(self, v):
        if v in self.vars:
            return self.vars[v]
        else:
            return int(v)

    def run(self, code):
        while self.pc < len(code):
            ins = code[self.pc][:3]
            args = code[self.pc][3:].split()
            self.pc += 1;
            self.ins[ins](*args)

        return self.vars

    def __ins_mov(self, a, b):
        self.vars[a] = self.get_value(b)

    def __ins_inc(self, a):
        self.vars[a] += 1

    def __ins_dec(self, a):
        self.vars[a] -= 1

    def __ins_jnz(self, a, b):
        if self.get_value(a) != 0:
            self.pc += self.get_value(b) - 1


def simple_assembler(program):
    # return a dictionary with the registers
    return Interpret().run(program)


a = ['mov c 12', 'mov b 0', 'mov a 200', 'dec a', 'inc b', 'jnz a -2', 'dec c', 'inc c', 'jnz c -2', 'mov c a']
code = ['mov a 5', 'inc a', 'dec a', 'dec a', 'jnz a -1', 'inc a']
simple_assembler(a)