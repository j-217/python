class FSM(object):
    def __init__(self, instructions):
        # Compile instructions string
        self.ins_dict = {}
        for ins in instructions.replace(';', ' ').replace(',', ' ').splitlines():
            if ins:
                name, z_ins, o_ins, outp = ins.split()[:4]
                self.ins_dict[name] = [z_ins, o_ins, int(outp)]


    def run_fsm(self, start, sequence):
        # return tuple: (final_state, final_state_output, path)
        final = start
        paths = [start]
        lst = []
        index = 0
        while index < len(sequence):
            if sequence[index] is 1:
                final = self.ins_dict[final][1]
                paths.append(final)
            if sequence[index] is 0:
                final = self.ins_dict[final][0]
                paths.append(final)
            index += 1
        final_outp = self.ins_dict[final][2]
        lst.append(final)
        lst.append(final_outp)
        lst.append(paths)
        print(self.lst)
        return tuple(lst)



instructions="""
UR; UR, UR; 61
ZPF; ZPF, ZPF; 43
cdST; UR, ZPF; 0
UR; UR, UR; 61
ZPF; ZPF, ZPF; 43
cdST; UR, ZPF; 0
"""
start = 'UR'
sequece = [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1]


f = FSM(instructions)
f.run_fsm(start, sequece)



