import string

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

def remove_red(s, c):
    s = s.replace(c, '')
    s = s.replace(c.upper(), '')
    return red(s)

def get_reduceds(s):
    reduceds = []
    for c in string.ascii_lowercase:
        reduceds.append(remove_red(s, c))
    return reduceds

with open('input.5') as f:
    polymer = f.read().splitlines()[0]

reduceds = get_reduceds(polymer)
print(min([len(r) for r in reduceds]))
