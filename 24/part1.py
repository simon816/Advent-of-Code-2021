import math
import operator
import sys

def perform_op_lit(op, state, dest, src):
    state[dest] = op(state[dest], src)

def perform_op_ind(op, state, dest, src):
    state[dest] = op(state[dest], state[src])

def operator_factory(op, args):
    dest, src = args
    if src in 'wxyz':
        return lambda state: perform_op_ind(op, state, dest, src)
    else:
        src = int(src)
        return lambda state: perform_op_lit(op, state, dest, src)

def read_in(state, invar):
    state[invar] = state['input'][state['inpos']]
    state['inpos'] += 1

def div(a, b):
    r = a / b
    if r < 0:
        return math.ceil(r)
    return math.floor(r)

program = []
for line in sys.stdin.readlines():
    op, *args = line.strip().split(' ')
    if op == 'inp':
        invar = args[0]
        program.append(lambda state: read_in(state, invar))
    elif op == 'add':
        program.append(operator_factory(operator.add, args))
    elif op == 'mul':
        program.append(operator_factory(operator.mul, args))
    elif op == 'div':
        program.append(operator_factory(div, args))
    elif op == 'mod':
        program.append(operator_factory(operator.mod, args))
    elif op == 'eql':
        program.append(operator_factory(lambda a,b: int(a==b), args))

tryval = [9, 4, 9, 9, 2, 9, 9, 2, 7, 9, 6, 1, 9, 9]
while True:
    for i in range(9, 0, -1):
        inp = list(tryval)
        inp.append(i)
        state = {'w': 0, 'x': 0, 'y': 0, 'z': 0, 'inpos': 0, 'input': inp}
        try:
            for insn in program:
                insn(state)
        except IndexError:
            pass
        print(state)
    break

