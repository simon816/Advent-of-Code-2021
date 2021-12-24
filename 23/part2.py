from collections import namedtuple
import functools
from queue import PriorityQueue
import sys

slot_names = ['slot_l1', 'slot_l2', 'slot_ab', 'slot_bc', 'slot_cd', 'slot_r1', 'slot_r2']

HEIGHT = 4

l_weights = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

class State(namedtuple('State', 'stack_a stack_b stack_c stack_d \
    slot_l1 slot_l2 slot_ab slot_bc slot_cd slot_r1 slot_r2')):

    def __repr__(self):
        return 'State(A=%s,B=%s,C=%s,D=%s slots=%s)' % (
            self.stack_a, self.stack_b, self.stack_c, self.stack_d,
            tuple(getattr(self, n) for n in slot_names)
        )
    
    def get_adjacent(self, ig=False):
        states = {}
        states.update(self.get_exit_stack_adj('stack_a', 1, 2))
        states.update(self.get_exit_stack_adj('stack_b', 2, 3))
        states.update(self.get_exit_stack_adj('stack_c', 3, 4))
        states.update(self.get_exit_stack_adj('stack_d', 4, 5))
        states.update(self.get_enter_stack_adj('stack_a', 'A', 1, 2, ig))
        states.update(self.get_enter_stack_adj('stack_b', 'B', 2, 3, ig))
        states.update(self.get_enter_stack_adj('stack_c', 'C', 3, 4, ig))
        states.update(self.get_enter_stack_adj('stack_d', 'D', 4, 5, ig))
        return states

    def get_enter_stack_adj(self, stack_label, require, left, right, ignore_invalid):
        states = {}
        stack = getattr(self, stack_label)
        if len(stack) < HEIGHT and (all(s == require for s in stack) or ignore_invalid):
            in_dist = HEIGHT - len(stack)
            for i, val, dist in self.enter_stack_blocked_by(left, right):
                if val == require or ignore_invalid:
                    replace = { slot_names[i]: None, stack_label: (require,) + stack }
                    state = self._replace(**replace)
                    cost = (dist + in_dist) * l_weights[val]
                    states[state] = cost
        return states

    def get_exit_stack_adj(self, stack_label, left, right):
        stack = getattr(self, stack_label)
        states = {}
        if stack:
            out_dist = (HEIGHT + 1) - len(stack)
            for i, dist in self.exit_stack_blocked_by(left, right).items():
                replace = { slot_names[i]: stack[0], stack_label: stack[1:]}
                state = self._replace(**replace)
                cost = (dist + out_dist) * l_weights[stack[0]]
                states[state] = cost
        return states

    # distance measured from the top space above the stack
    def exit_stack_blocked_by(self, left, right):
        slots = [self.slot_l1, self.slot_l2, self.slot_ab, self.slot_bc, self.slot_cd, self.slot_r1, self.slot_r2]
        accessible = {}
        distance = 1
        for i in range(left, -1, -1):
            if slots[i] is not None:
                break
            accessible[i] = distance
            distance += 2 if i > 1 else 1
        distance = 1
        for i in range(right, len(slots)):
            if slots[i] is not None:
                break
            accessible[i] = distance
            distance += 2 if i < 5 else 1
        return accessible

    def enter_stack_blocked_by(self, left, right):
        slots = [self.slot_l1, self.slot_l2, self.slot_ab, self.slot_bc, self.slot_cd, self.slot_r1, self.slot_r2]
        distance = 1
        first_left = None
        for i in range(left, -1, -1):
            if slots[i] is not None:
                first_left = i
                break
            distance += 2 if i > 1 else 1
        if first_left is not None:
            yield first_left, slots[first_left], distance
        distance = 1
        first_right = None
        for i in range(right, len(slots)):
            if slots[i] is not None:
                first_right = i
                break
            distance += 2 if i < 5 else 1
        if first_right is not None:
            yield first_right, slots[first_right], distance

sys.stdin.readline()
sys.stdin.readline()
l1 = sys.stdin.readline().strip().replace('#', '')
l2 = sys.stdin.readline().strip().replace('#', '')

insert = ['DCBA', 'DBAC']

stacks = list(zip(l1, *insert, l2))

initial_state = State(
    stack_a = stacks[0],
    stack_b = stacks[1],
    stack_c = stacks[2],
    stack_d = stacks[3],
    slot_l1 = None,
    slot_l2 = None,
    slot_ab = None,
    slot_bc = None,
    slot_cd = None,
    slot_r1 = None,
    slot_r2 = None,
)

final_state = State(
    stack_a = ('A',) * HEIGHT,
    stack_b = ('B',) * HEIGHT,
    stack_c = ('C',) * HEIGHT,
    stack_d = ('D',) * HEIGHT,
    slot_l1 = None,
    slot_l2 = None,
    slot_ab = None,
    slot_bc = None,
    slot_cd = None,
    slot_r1 = None,
    slot_r2 = None,
)

node = initial_state
weights = { initial_state: 0 }
permanents = set()
curr_dist = 0

queue = PriorityQueue()

@functools.total_ordering
class Item(namedtuple('Item', 'pri data')):

    def __lt__(self, other):
        assert type(other) == Item
        return self.pri < other.pri

    def __eq__(self, other):
        assert type(other) == Item
        return self.pri == other.pri

while node != final_state:
    curr_dist = weights[node] = min(curr_dist, weights[node])
    permanents.add(node)
    for adj, cost in node.get_adjacent().items():
        if adj in permanents:
            continue
        if adj in weights:
            weights[adj] = min(weights[adj], curr_dist + cost)
        else:
            weights[adj] = curr_dist + cost
        queue.put(Item(weights[adj], adj))
    while node in permanents:
        lowest, node = queue.get()
    curr_dist += lowest

print(min(curr_dist, weights[node]))
