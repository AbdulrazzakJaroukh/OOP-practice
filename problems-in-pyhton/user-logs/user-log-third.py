import pandas as pd
from datetime import datetime
from datetime import timedelta
from operator import itemgetter


def change_string_to_time(s):
    return datetime.fromisoformat(s.replace('_', 'T'))


def count_events_in_20_interval(date_list):
    count = 1
    start = date_list[0]
    if len(date_list) <= 1:
        return start, count
    k = 1
    while date_list[k] <= start + timedelta(minutes=20):
        count += 1
        k += 1
        if k >= len(date_list):
            break
    return start, count


columns = ['date', 'user', 'event_type', 'parameter']
df = pd.read_csv("log.csv", usecols=columns)

date_column = df.to_numpy()[:, 0].tolist()
users_column = df.to_numpy()[:, 1].tolist()
type_column = df.to_numpy()[:, 2].tolist()
param_column = df.to_numpy()[:, 3].tolist()

date_column_converted_all = list(map(change_string_to_time, date_column))

# print(create_lists_in_20_intervals(date_column_converted_all)[0])

# print(count_events_in_20_interval(date_column_converted_all))

start_count = []
for i in range(len(date_column_converted_all)-199990):
    start_count.append(count_events_in_20_interval(date_column_converted_all[i:]))

# print(start_count)

print(max(start_count, key=itemgetter(1)))

max_elements = list(filter(lambda x: x if x[1] == 230 else None, start_count))
# take the last in time
