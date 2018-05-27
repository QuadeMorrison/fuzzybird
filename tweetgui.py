#!/usr/bin/env python3

import config
import twitter
import soundex
import unicodedata
import config
import curses
import string
import shutil
import signal, sys

g_lines, g_cols = 0, 0
g_hashtags, g_encoded_hashtags = [], []

START_CURSOR_X=2

tweet_arr = ["aeou", "bob", "bill", "quade", "colton", "alan"]
cursor_x, cursor_y = 0, 0

spot = 0

input_string = ""
finish_winch = False

char_codes = []
for c in string.printable:
    char_codes.append(ord(c))

def draw_scr(stdscr):
    global input_string, g_hashtags, g_encoded_hashtags, tweet_arr, spot

    # update array, update spot, draw
    tweet_arr = soundex.match(input_string, g_hashtags, g_encoded_hashtags)
    tl = len(tweet_arr) - 1
    if tl < 0:
        spot = -1
    else:
        spot = min(tl, max(0, spot))

    # draw stuff
    stdscr.move(0, 0)
    stdscr.clear()

    cursor_y = curses.LINES-1
    stdscr.move(cursor_y, cursor_x)

    for i, tw in enumerate(tweet_arr):
        if i < curses.LINES-1:
            stdscr.addnstr(curses.LINES-2-i, START_CURSOR_X, tw, curses.COLS-1-START_CURSOR_X)
        else:
            break

    if spot >= 0:
        stdscr.addnstr(curses.LINES-2-spot, 0, "> ", START_CURSOR_X)

    stdscr.addnstr(curses.LINES-1, 0, "> " + input_string, curses.COLS-1)
    stdscr.refresh()

def main(stdscr):
    cursor_x = START_CURSOR_X
    cursor_y = curses.LINES-1
    global spot, input_string, finish_winch, g_lines, g_cols
    global input_string, g_hashtags, g_encoded_hashtags, tweet_arr

    draw_scr(stdscr)

    while True:
        ch_code = stdscr.getch()
        if ch_code == curses.KEY_UP:
            spot = min(len(tweet_arr)-1, curses.LINES-2, spot + 1)
        elif ch_code == curses.KEY_DOWN:
            spot = max(0, spot - 1)
        elif ch_code == 8 or ch_code == 127:
            cursor_x = max(START_CURSOR_X, cursor_x - 1)
            input_string = input_string[:-1]
        elif ch_code == 10:
            # enter key
            break
        elif ch_code in char_codes and cursor_x < curses.COLS-1:
            cursor_x += 1
            input_string += chr(ch_code)
        elif ch_code == curses.KEY_RESIZE:
            # Assume WINCH
            input_string = ""
            cursor_x = START_CURSOR_X
            spot = 0
            l, c = stdscr.getmaxyx()
            if g_lines != l or g_cols != c:
                curses.resizeterm(l, c)
                g_lines, g_cols = l, c

        draw_scr(stdscr)

def execute(hashtags, encoded_hashtags):
    global g_hashtags, g_encoded_hashtags
    g_hashtags, g_encoded_hashtags = hashtags, encoded_hashtags
    curses.wrapper(main)

    if spot >= 0:
        print(tweet_arr[spot])
