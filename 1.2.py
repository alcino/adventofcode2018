import pandas as pd
from collections import defaultdict

def find_frequency(adjustments):
    start_freq = 0
    freq_counts = defaultdict(int)
    while True:
        freqs = start_freq + adjustments.cumsum()
        start_freq = freqs.iloc[-1]
        for k, v in freqs.iteritems():
            freq_counts[v] += 1
            if freq_counts[v] > 1:
                return v

adjustments = pd.read_csv('input.1', header=None)[0]
print(find_frequency(adjustments))
