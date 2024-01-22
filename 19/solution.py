import re
from math import prod
from operator import lt, gt
import portion as P
from copy import deepcopy

with open('test.txt') as f:
    txt = f.read()

workflows, parts = txt.split('\n\n')

x = 'x'; m = 'm'; a = 'a'; s = 's'
parts = [eval(p.replace('=', ':')) for p in parts.split('\n')]
del x, m, a, s

# part 1

def accept(p):
    def wf(l):
        f = workflows[l]
        for ff in f.split(','):
            ff_parts = ff.split(':')
            if len(ff_parts) == 2:
                if_, then = ff_parts
                c = if_[0]
                o = lt if if_[1] == '<' else gt
                i = int(if_[2:])

                if o(p[c], i):
                    return False if then == 'R' else True if then == 'A' else wf(then)
            else:
                label = ff_parts[0]
                return False if label == 'R' else True if label == 'A' else wf(label)

    return wf('in')

d = {}
for w in workflows.split('\n'):
    label, func = re.match('^(\w+)\{(.+?)\}$', w).groups()
    d[label] = func
workflows = d
del d

print(sum(sum(p.values()) for p in parts if accept(p)))

# part 2: keep track of which logic leads to True

def wf2(l, bounds):
    f = workflows[l]
    count = 0

    for ff in f.split(','):
        ff_parts = ff.split(':')
        if len(ff_parts) == 2:
            if_, then = ff_parts
            c = if_[0]
            o = lt if if_[1] == '<' else gt
            i = int(if_[2:])

            if then != 'R':
                then_bounds = deepcopy(bounds)
                then_bounds[c] &= P.openclosed(i, then_bounds[c].upper) if o == gt else P.closedopen(then_bounds[c].lower, i)
                if any(b.empty for b in then_bounds.values()):
                    break

                if then == 'A':
                    count += prod(len(list(P.iterate(b, step=1))) for b in then_bounds.values())
                else:
                    count += wf2(then, then_bounds)

            if o == lt:
                bounds[c] &= P.closed(i, bounds[c].upper)
            else:
                bounds[c] &= P.closed(bounds[c].lower, i)

            if any(b.empty for b in bounds.values()):
                break
        else:
            label = ff_parts[0]
            if label != 'R':
                if label == 'A':
                    count += prod(len(list(P.iterate(b, step=1))) for b in bounds.values())
                else:
                    count += wf2(label, bounds)

    return count

print(wf2('in', {k : P.closed(1, 4000) for k in 'xmas'}))