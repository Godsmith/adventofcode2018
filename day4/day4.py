from collections import Counter
from typing import Dict
from .. import util


def parse_guard_id(line):
    return int(line.split(' ')[3][1:])

def guard_ids(lines):
    for line in lines:
        if '#' in line:
            yield parse_guard_id(line)

def time(line):
    return int(line.split(':')[1].split(']')[0])


def calculate_guard_sleep_time(records):
    guard_id = ''
    sleep_time = 0
    guard_sleep_time = Counter()
    for line in records:
        if '#' in line:
            guard_id = parse_guard_id(line)
        elif 'sleep' in line:
            sleep_time = time(line)
        elif 'wake' in line:
            guard_sleep_time[guard_id] += time(line) - sleep_time
    return guard_sleep_time


def calculate_guard_most_likely_sleep_minute(records, id):
    sleep_from_minute = Counter()
    sleep_time = ''
    collect = False
    for line in records:
        if '#' in line:
            collect = parse_guard_id(line) == id
        if collect:
            if 'sleep' in line:
                sleep_time = time(line)
            elif 'wake' in line:
                for i in range(sleep_time, time(line)):
                    sleep_from_minute[i] += 1
    return sleep_from_minute


def key_for_largest_value(dict_: Dict):
    return list(key for key, value in dict_.items() if value == max(
        dict_.values()))[0]


lines = sorted(util.input_lines(4))

RECORDS = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""".splitlines()

# Part 1

sleep_time_from_guard_id = calculate_guard_sleep_time(lines)
guard_most_asleep = key_for_largest_value(sleep_time_from_guard_id)
sleep_from_minute = calculate_guard_most_likely_sleep_minute(lines,
                                                             guard_most_asleep)
time_asleep = key_for_largest_value(sleep_from_minute)
print(guard_most_asleep * time_asleep)

guard_with_record_sleep_minute = ''
record_sleep_times = 0
record_sleep_minute = ''

# Part 2
for id in guard_ids(lines):
    sleep_from_minute = calculate_guard_most_likely_sleep_minute(lines, id)
    if sleep_from_minute:
        if max(sleep_from_minute.values()) > record_sleep_times:
            record_sleep_times = max(sleep_from_minute.values())
            guard_with_record_sleep_minute = id
            record_sleep_minute = key_for_largest_value(sleep_from_minute)

print(guard_with_record_sleep_minute * record_sleep_minute)





# print(time('[1518-11-01 00:00] Guard #10 begins shift'))
