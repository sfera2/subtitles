from math import floor


def get_lines(file):
    try:
        with open(file) as files:
            for line in files:
                yield line
    except UnicodeDecodeError:
        with open(file, encoding='windows-1250') as files:
            for line in files:
                yield line




def hours(time):
    hour, minute, second = time.split(':')
    second, milisecond = second.split(',') if ',' in second else (second, 0)
    return int(hour), int(minute), int(second), int(milisecond)


def count_seconds(hour, minute, seconds, miliseconds):
    return 60*60*hour + 60*minute + seconds + miliseconds//1000


def seconds_into_hour(num_of_seconds):
    hour = int(num_of_seconds//(60*60))
    num_of_seconds -= hour * 60 * 60
    minute = int(num_of_seconds//60)
    num_of_seconds -= minute * 60
    second = floor(num_of_seconds)
    num_of_seconds -= second
    milisecond = floor(num_of_seconds * 1000)
    if hour < 10: hour = f'0{hour}'
    if minute < 10: minute = f'0{minute}'
    if second < 10: second = f'0{second}'
    if milisecond < 10: milisecond = f'00{milisecond}'
    elif milisecond < 100: milisecond = f'0{milisecond}'
    return f'{hour}:{minute}:{second},{milisecond}'


def polish_characters(line):
    mappping = {
        'ê': 'ę',
        'Ê': 'Ę',
        '³': 'ł',
        '¿': 'ż',
        '': 'ś',
        '¹': 'ą',
        '¯': 'Ż',
    }
    for k, v in mappping.items():
        line = line.replace(k, v)
    return line