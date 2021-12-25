import math
import operator
import sys

def div(a, b):
    r = a / b
    if r < 0:
        return math.ceil(r)
    return math.floor(r)

INPUT = 'INPUT'

def optree(args, op):
    dest, src = args
    if src not in 'wxyz':
        src = int(src)
    return ('set', dest, (op, dest, src))

program = []
for line in sys.stdin.readlines():
    op, *args = line.strip().split(' ')
    if op == 'inp':
        invar = args[0]
        program.append(('set', invar, INPUT))
    elif op == 'add':
        program.append(optree(args, '+'))
    elif op == 'mul':
        program.append(optree(args, '*'))
    elif op == 'div':
        program.append(optree(args, '/'))
    elif op == 'mod':
        program.append(optree(args, '%'))
    elif op == 'eql':
        program.append(optree(args, '=='))

def reduce_expr(state, expr):
    if expr == INPUT:
        return expr, True
    if type(expr) == str and expr in 'wxyz':
        state['reads'].add(expr)
        ci = expr in state['contains_input']
        if state[expr] is not None:
            return state[expr], ci
        return expr, ci
    if type(expr) == int:
        return expr, False
    op, left, right = expr
    left, lci = reduce_expr(state, left)
    right, rci = reduce_expr(state, right)
    eval_fn = None
    if op == '*':
        if left == 0 or right == 0:
            return 0, False
        if left == 1:
            return right, rci
        if right == 1:
            return left, lci
        eval_fn = operator.mul
    elif op == '+':
        if left == 0:
            return right, rci
        if right == 0:
            return left, lci
        eval_fn = operator.add
    elif op == '%':
        assert right != 0
        if left == 0:
            return 0, False
        eval_fn = operator.mod
    elif op == '/':
        assert right != 0
        if right == 1:
            return left, lci
        eval_fn = div
    elif op == '==':
        if type(left) == str and left in 'wxyz' and left == right:
            return 1, False
        # special case
        if left == 'w' and type(right) == int and (right > 9 or right < 1):
            return 0, False
        if right == 'w' and type(left) == int and (left > 9 or left < 1):
            return 0, False
        eval_fn = lambda a, b: int(a == b)

    if type(left) == int and type(right) == int:
        return eval_fn(left, right), False

    return (op, left, right), rci or lci

def print_expr(expr):
    if expr == INPUT:
        return 'INPUT'
    if type(expr) == str and expr in 'wxyz':
        return expr
    if type(expr) == int:
        return str(expr)
    op, left, right = expr
    return '(' + print_expr(left) + ' ' + op + ' ' + print_expr(right) + ')'

prog = program
changed = True
while changed:
    changed = False
    var_states = {'w': 0, 'x': 0, 'y': 0, 'z': 0, 'contains_input': set(),
                  'reads': set()}
    new_prog = []
    most_recent_set = {}
    dead = set()
    for stmt in prog:
        assert stmt[0] == 'set'
        _, var, expr = stmt
        new_expr, ci = reduce_expr(var_states, expr)
        if type(new_expr) == int:
            var_states[var] = new_expr
        else:
            if ci:
                var_states['contains_input'].add(var)
            if var not in var_states['contains_input']:
                var_states[var] = new_expr
            else:
                var_states[var] = None
        if new_expr != expr:
            changed = True
        new_stmt = ('set', var, new_expr)
        new_prog.append(new_stmt)
        if var not in var_states['reads'] and var in most_recent_set:
            dead.add(most_recent_set[var])
        most_recent_set[var] = new_stmt
        if var == new_expr:
            dead.add(new_stmt)
        if var in var_states['reads']:
            var_states['reads'].remove(var)
    prog = [s for s in new_prog if s not in dead]

for stmt in prog:
    print(stmt[1], '=', print_expr(stmt[2]))
