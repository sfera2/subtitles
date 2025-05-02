import argparse
import os.path
from Utils import get_lines
from Utils import hours
from Utils import count_seconds
from Utils import seconds_into_hour
from Utils import polish_characters
from FindParameters import calculate_ratio
from FindParameters import calculate_offset



def change_frame_rate(seconds):
    return seconds * RATIO - OFFSET


def process_line(line):
    if ' --> ' in line:
        line = polish_characters(line)
        start, end = line.split(' --> ')
        start_time, end_time = hours(start), hours(end)
        start_seconds, end_seconds = count_seconds(*start_time), count_seconds(*end_time)
        start_seconds_updated = change_frame_rate(start_seconds)
        end_seconds_updated = change_frame_rate(end_seconds)
        new_start_text = seconds_into_hour(start_seconds_updated)
        new_end_text = seconds_into_hour(end_seconds_updated)
        return f'{new_start_text} --> {new_end_text}'
    return line.strip()


def change_lines():
    new_file_name = f'Improved_{os.path.basename(FILE)}'
    new_file = os.path.join(os.path.dirname(FILE), new_file_name)
    with open(new_file, 'w') as files:
        lines = get_lines(FILE)
        for line in lines:
            line = process_line(line)
            print(line, file=files)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # parser.add_argument('file', type=str)
    # parser.add_argument('original_framerate', type=int)
    # parser.add_argument('new_framerate', type=int)
    # parser.add_argument('delay', default=0, type=int, help="Int. How much to delay subs. Negative numbers allowed to make them ahead")

    # args = parser.parse_args()

    # DELAY = args.delay
    # ORIGINAL_FRAMERATE = args.original_framerate
    # NEW_FRAMERATE = args.new_framerate
    # FILE = args.file
    # FILE = r'~/Downloads/La.cara.oculta.2011.DVDRip.XviD.5rFF/Subs/The.Hidden.Face.2011.720p.BluRay.x264.DTS-engm.srt'

    # line1 = input('Give me some line ')
    # time1 = input('Give me time in 00:00:00 format ')
    # line2 = input('Give me other line ')
    # time2 = input('Give me time in 00:00:00 format ')

    direc = r'~/Downloads/the.last.of.the.mohicans.(1992).pol.1cd.(5044011)NapisyPol.srt'
    FILE = r'~/Downloads/the.last.of.the.mohicans.(1992).pol.1cd.(5044011)NapisyPol.srt'
    # print(os.listdir(direc))
    # FILE = r'/NapisyPol.srt'
    correct_line1 = ('TRZECI ROK WOJNY', '00:00:26')
    correct_line2 = ('Horican jest prawie pusty', '00:05:41')

    # correct_line1 = (line1, time1)
    # correct_line2 = (line2, time2)
    #
    RATIO = calculate_ratio(FILE, correct_line1, correct_line2)
    OFFSET = calculate_offset(FILE, correct_line1, RATIO)

    change_lines()



