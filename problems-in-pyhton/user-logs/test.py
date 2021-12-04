

dict = {}

dict['1'] = []
dict['1'] = []
dict['2'] = []
print(dict)


def extract_user_events_sequence_started_in_18(events_list):
    events_list_start_18 = []
    if not events_list:
        return events_list_start_18
    if len(events_list) > 1:
        if events_list[0] < change_string_to_time('2020-04-19_00:00:00'):
            events_list_start_18.append(events_list[0])
            for i in range(len(events_list) - 1):
                success_to_add = test_two_followed_events(events_list[i], events_list[i+1])
                if success_to_add:
                    events_list_start_18.append(events_list[i+1])
                else:
                    break
    else:
        if events_list[0] < change_string_to_time('2020-04-19_00:00:00'):
            events_list_start_18.append(events_list[0])
    return events_list_start_18




# print(type(date[0]))
# print(change_time_to_struct(date[0]))
# time_obj = change_string_to_time(date_column[0])
# time_obj1 = change_string_to_time(date_column[1])
# print(time_obj - time_obj1)
# print(len(dict_users))
# print(date_column_converted[0]+timedelta(minutes=30))
# print(date_column[0])
# print(dict_users[users_column[0]][25:30])
# session = count_sessions_for_a_user(dict_users[users_column[0]][25:30])
# print(session)