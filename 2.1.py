import pandas as pd
from collections import defaultdict

def count_letters(s):
    counts = defaultdict(int)
    for l in s:
        counts[l] += 1
    return counts

def sum_n(count_series, n):
    return count_series.apply(lambda x: any([v == n for v in x.values()])).sum()

def checksum(count_series):
    return sum_n(count_series, 2)*sum_n(count_series, 3)

ids = pd.read_csv('input.2', header=None)[0]
count_series = ids.apply(count_letters)
print(checksum(count_series))
