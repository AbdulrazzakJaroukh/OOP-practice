import pandas as pd
from datetime import datetime
from datetime import timedelta


def change_string_to_time(s):
    return datetime.fromisoformat(s.replace('_', 'T'))


def test_two_followed_events(event1, event2):
    if event1 + timedelta(minutes=30) > event2:
        return True
    elif event2 < change_string_to_time('2020-04-19_00:00:00'):
        return True
    else:
        return False


def extract_user_events_sequence_started_in_18(events_list):
    events_list_start_18 = []
    if events_list[0] < change_string_to_time('2020-04-19_00:00:00'):
        events_list_start_18.append(events_list[0])
        for i in range(len(events_list) - 1):
            success_to_add = test_two_followed_events(events_list[i], events_list[i+1])
            if success_to_add:
                events_list_start_18.append(events_list[i+1])
            else:
                break
    return events_list_start_18


def count_sessions_for_a_user(events_list):
    sessions = 1
    for i in range(len(events_list)-1):
        if events_list[i] + timedelta(minutes=30) <= events_list[i+1]:
            sessions += 1
    return sessions


columns = ['date', 'user']
df = pd.read_csv("log.csv", usecols=columns)

users_column = df.to_numpy()[:, 1].tolist()
date_column = df.to_numpy()[:, 0].tolist()
date_column_converted_all = list(map(change_string_to_time, date_column))

date_column_converted_18 = [e for e in date_column_converted_all if e >= change_string_to_time('2020-04-18_00:00:00')]

date_user = list(zip(users_column, date_column_converted_18))

dict_users = {}
for user in users_column:
    dict_users[user] = []

for user, date in date_user:
    dict_users[user].append(date)

for user in dict_users:
    dict_users[user] = sorted(dict_users[user])

total_sessions_st_18 = 0
for user in dict_users:
    dict_users[user] = extract_user_events_sequence_started_in_18(dict_users[user])
    total_sessions_st_18 += count_sessions_for_a_user(dict_users[user])


test_list = [datetime(2020, 4, 17, 10, 22, 14), datetime(2020, 4, 18, 23, 59, 59), datetime(2020, 4, 19, 0, 29, 14), datetime(2020, 4, 19, 0, 59, 13)]
print(count_sessions_for_a_user(dict_users[631169]))
print(extract_user_events_sequence_started_in_18(test_list))
print(total_sessions_st_18)
print(dict_users[631169])
