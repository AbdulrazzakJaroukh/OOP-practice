import pandas as pd
from datetime import datetime
from datetime import timedelta


def change_string_to_time(s):
    return datetime.fromisoformat(s.replace('_', 'T'))


columns = ['date', 'user', 'event_type', 'parameter']
df = pd.read_csv("log.csv", usecols=columns)

date_column = df.to_numpy()[:, 0].tolist()
users_column = df.to_numpy()[:, 1].tolist()
type_column = df.to_numpy()[:, 2].tolist()
param_column = df.to_numpy()[:, 3].tolist()

date_column_converted_all = list(map(change_string_to_time, date_column))

four_element_data = list(zip(date_column_converted_all, users_column, type_column, param_column))
filtered_1_four_element_data = list(filter(lambda element: element if element[2] == 4 else None, four_element_data))
filtered_2_four_element_data = list(filter(lambda element: element if element[3] == 'text' else None, filtered_1_four_element_data))
print(date_column_converted_all[0].date())

dict_days = {}
for item in filtered_2_four_element_data:
    dict_days[item[0].date()] = []

for item in filtered_2_four_element_data:
    dict_days[item[0].date()].append(item[1])

filtered_dict_days = {}
for day in dict_days:
    filtered_dict_days[day] = list(dict.fromkeys(dict_days[day]))

numbers = []
for day in filtered_dict_days:
    numbers.append(len(filtered_dict_days[day]))

print(filtered_dict_days)
print(max(numbers))
