import numpy as np
import pandas as pd
from collections import namedtuple

def parse_data(data):
    parsed_data = []
    Record = namedtuple('Record', ('claim', 'start_x', 'start_y', 'size_x', 'size_y'))
    for d in data:
        claim, _, start, size = d.split()
        claim = claim[1:]
        start_x, start_y = map(int, start[:-1].split(','))
        size_x, size_y = map(int, size.split('x'))
        parsed_data.append(Record(claim, start_x, start_y, size_x, size_y))
    return parsed_data

def build_coordinates(parsed_data):
    df = pd.DataFrame(parsed_data)
    df['end_x'] = df['start_x'] + df['size_x']
    df['end_y'] = df['start_y'] + df['size_y']
    return df

def build_fabric(df):
    fabric = np.zeros((1000, 1000))
    for _, row in df.iterrows():
        fabric[row['start_x']:row['end_x'], row['start_y']:row['end_y']] += 1
    return fabric

def check_claims(df, fabric):
    for _, row in df.iterrows():
        if (fabric[row['start_x']:row['end_x'], row['start_y']:row['end_y']] == 1).all():
            return row['claim']

with open('input.3') as f:
    data = f.read().splitlines()
data = parse_data(data)
df = build_coordinates(data)
fabric = build_fabric(df)
print(check_claims(df, fabric))
