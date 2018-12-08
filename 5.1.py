def is_pair(a, b):
    return (a != b) and (a.lower() == b.lower())

def react(ab):
    if is_pair(ab[0], ab[1]):
        return ''
    else:
        return ab

def red(s):
    i = 0
    l = len(s) - 1
    while i < l:
        pair = s[i:i+2]
        reaction = react(pair)
        if pair == reaction:
            i += 1
        else:
            s = s[:i] + s[i+2:]
            l = len(s) - 1
            i = max(0, i-1)
    return s

with open('input.5') as f:
    polymer = f.read().splitlines()[0]

print(len(red(polymer)))
