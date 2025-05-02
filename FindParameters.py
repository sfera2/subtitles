import re
from Utils import get_lines
from Utils import hours
from Utils import count_seconds


def get_time(line_time: str):
    return line_time.split(' --> ')[0]


def original_time(file, searched_line):
    time_patt = re.compile(r'.*\d\d:\d\d:\d\d.*')
    new_line_flag = False
    for line in get_lines(file):
        if time_patt.match(line):
            new_line_flag = True
            current_time = get_time(line)
            continue
        if new_line_flag:
            new_line_flag = False
            if line.startswith(searched_line): return current_time


def calculate_ratio(file, correct_line1, correct_line2):
    bad_time1 = original_time(file, correct_line1[0])
    bad_time2 = original_time(file, correct_line2[0])

    good_time1_int = count_seconds(*hours(correct_line1[1]))
    good_time2_int = count_seconds(*hours(correct_line2[1]))
    bad_time1_int = count_seconds(*hours(bad_time1))
    bad_time2_int = count_seconds(*hours(bad_time2))

    ratio = (good_time2_int - good_time1_int)/(bad_time2_int - bad_time1_int)
    return ratio


def calculate_offset(file, correct_line1, ratio):
    bad_time1 = original_time(file, correct_line1[0])
    good_time1_int = count_seconds(*hours(correct_line1[1]))
    bad_time1_int = count_seconds(*hours(bad_time1))

    bad_time_ratio_adjusted = bad_time1_int * ratio
    return bad_time_ratio_adjusted - good_time1_int


if __name__ == '__main__':
    file = r'~/Downloads/the.last.of.the.mohicans.\(1992\).pol.1cd.\(5044011\)/The\ Last\ of\ the\ Mohicans.srt'
    correct_line1 = ('TRZECI ROK WOJNY', '00:00:26')
    correct_line2 = ('Horican jest prawie pusty', '00:05:41')

    ratio = calculate_ratio(file, correct_line1, correct_line2)
    offset = calculate_offset(file, correct_line1, ratio)

    print(ratio)
    print(offset)

