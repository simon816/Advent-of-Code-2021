import sys

debug = lambda *args: None
#debug = print

class Number:

    def __init__(self, left, right):
        self.parent = None
        self.left = left
        self.right = right
        if isinstance(left, Number):
            left.parent = self
        if isinstance(right, Number):
            right.parent = self

    def __repr__(self):
        return '[%s,%s]' % (self.left, self.right)

    def __add__(self, other):
        assert self.parent is other.parent, (self.parent, other.parent)
        new_num = Number(self, other)
        new_num.reduce()
        return new_num

    def magnitude(self):
        left = self.left if type(self.left) == int else self.left.magnitude()
        right = self.right if type(self.right) == int else self.right.magnitude()
        return left*3 + right*2

    def last_left(self):
        look = self
        debug("find first left of", look)
        while look.parent.left is look:
            debug(look, "is on the left of", look.parent)
            look = look.parent
            if not look.parent:
                debug("no parent")
                return None, None
        if type(look.parent.left) == int:
            debug("[left] using parent left", look.parent)
            return look.parent, 'left'
        debug("[left] get last right of", look.parent.left)
        return look.parent.left.last_right()

    def last_right(self):
        if type(self.right) == int:
            return self, 'right'
        return self.right.last_right()

    def first_right(self):
        look = self
        debug("find first right of", look)
        while look.parent.right is look:
            debug(look, "is on the right of", look.parent)
            look = look.parent
            if not look.parent:
                debug("no parent")
                return None, None
        if type(look.parent.right) == int:
            debug("[right] using parent right", look.parent)
            return look.parent, 'right'
        debug("[right] get first left of", look.parent.right)
        return look.parent.right.first_left()

    def first_left(self):
        if type(self.left) == int:
            return self, 'left'
        return self.left.first_left()

    def reduce(self):
        bail = True
        while bail:
            bail = True
            while bail:
                debug("stage", self)
                _, bail = self.reduce1()
            _, bail = self.reduce1(do_split=True)
        debug("final", self)

    def reduce1(self, nesting_level=0, do_split=False):
        if nesting_level == 4:
            assert type(self.left) == type(self.right) == int, self
            llh, lla = self.last_left()
            frh, fra = self.first_right()
            debug("EXPLODE", self, (llh, lla), (frh, fra))
            if llh:
                if lla == 'left':
                    llh.left += self.left
                else:
                    llh.right += self.left
            if frh:
                if fra == 'left':
                    frh.left += self.right
                else:
                    frh.right += self.right
            return 0, True
        if isinstance(self.left, Number):
            new_val, bail = self.left.reduce1(nesting_level + 1, do_split)
            if new_val is not None:
                self.left = new_val
                return None, True
            if bail:
                return None, True
        elif do_split:
            if self.left > 9:
                debug("SPLIT", self.left)
                self.left = split(self, self.left)
                return None, True
        if isinstance(self.right, Number):
            new_val, bail = self.right.reduce1(nesting_level + 1, do_split)
            if new_val is not None:
                self.right = new_val
                return None, True
            if bail:
                return None, True
        elif do_split:
            if self.right > 9:
                debug("SPLIT", self.right)
                self.right = split(self, self.right)
                return None, True
        return None, False

def split(parent, val):
    left = int(val / 2)
    right = val - left
    val = Number(left, right)
    val.parent = parent
    return val


class NumberBuilder:

    def __init__(self):
        self.nums = []

    def push_number(self, num):
        if len(self.nums) == 2:
            self.nums[-1] *= 10
            self.nums[-1] += num
            return
        self.nums.append(num)

    def move_right(self):
        assert len(self.nums) == 1, self.nums

    def build(self):
        assert len(self.nums) == 2, self.nums
        return Number(*self.nums)

result = None

for line in sys.stdin.readlines():
    stack = [NumberBuilder()]
    for c in line.strip():
        if c == '[':
            stack.append(NumberBuilder())
        elif c == ']':
            b = stack.pop()
            stack[-1].push_number(b.build())
        elif c == ',':
            stack[-1].move_right()
        else:
            stack[-1].push_number(int(c))
    assert len(stack) == 1
    stack[0].move_right()
    number = stack[0].nums[0]
    if result is None:
        result = number
    else:
        result = result + number
print(result.magnitude())
