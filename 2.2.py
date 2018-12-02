import pandas as pd

def distance(s1, s2):
    return sum([l1 != l2 for l1, l2 in zip(s1, s2)])

def is_close(s1, s2):
    return distance(s1, s2) == 1

def find_close(ids):
    for i in range(len(ids)):
        for j in range(i, len(ids)):
            if is_close(ids[i], ids[j]):
                return ids[i], ids[j]

def common_chars(s1, s2):
    return ''.join([l1 for l1, l2 in zip(s1, s2) if l1 == l2])

ids = pd.read_csv('input.2', header=None)[0]
print(common_chars(*find_close(ids)))
