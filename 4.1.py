import re
import numpy as np
import pandas as pd

def build_df(data):
    ts_labels = ['year', 'month', 'day', 'hour', 'minute']
    r = re.compile('\[(.*)-(.*)-(.*) (.*):(.*)\] (.*)')
    df = pd.DataFrame(
        [*map(lambda x: r.match(x).groups(), data)],
        columns=ts_labels + ['action']
    )
    df[ts_labels] = df[ts_labels].astype(np.int64)
    df['year'] += 500
    df['timestamp'] = df[ts_labels].apply(lambda x: pd.datetime(*x), axis=1)
    df = df.sort_values('timestamp')
    before_midnight = df.loc[df['timestamp'].dt.hour >= 1, 'timestamp']
    before_midnight = pd.to_datetime(before_midnight.dt.date) + pd.Timedelta('1D')
    df.loc[df['timestamp'].dt.hour >= 1, 'timestamp'] = before_midnight
    df['guard'] = df['action'].str.extract('.*#([0-9]+).*').fillna(method='ffill').astype(np.int64)
    return df

def get_sleeps(df):
    guard = df[['guard']][df['action'] == 'falls asleep'].reset_index(drop=True)
    sleep = df[['minute']][df['action'] == 'falls asleep'].reset_index(drop=True)
    wake = df[['minute']][df['action'] == 'wakes up'].reset_index(drop=True)
    sleep.columns = ['sleep']
    wake.columns = ['wake']
    snooze = pd.concat([guard, sleep, wake], axis=1)
    snooze['duration'] = snooze['wake'] - snooze['sleep']
    return snooze

def build_schedule(snooze):
    schedule = np.zeros((len(snooze), 60))
    for i in range(len(snooze)):
        schedule[i, snooze.iloc[i]['sleep']:snooze.iloc[i]['wake']] = 1
    schedule = pd.concat([snooze[['guard']], pd.DataFrame(schedule)], axis=1)
    return schedule.groupby('guard').sum()

with open('input.4') as f:
    data = f.read().splitlines()

df = build_df(data)
snooze = get_sleeps(df)
schedule = build_schedule(snooze)
guard = schedule.sum(axis=1).idxmax()
minute = schedule.loc[guard].idxmax()
print(guard*minute)
