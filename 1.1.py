import pandas as pd
adjustments = pd.read_csv('input.1', header=None)[0]
print(adjustments.sum().iloc[0])
