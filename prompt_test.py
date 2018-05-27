#!/usr/bin/env python3

import curses
import string
from curses import wrapper

START_CURSOR_X=2

tweet_arr = ["asoueth", "bob", "bill", "quade", "colton", "alan"]
cursor_x, cursor_y = 0, 0

spot = 0

def draw_scr(stdscr, input_str):
    stdscr.clear()

    for i, tw in enumerate(tweet_arr):
        if i < curses.LINES-1:
            stdscr.addnstr(curses.LINES-2-i, START_CURSOR_X, tw, curses.COLS-1-START_CURSOR_X)
        else:
            break

    if spot >= 0:
        stdscr.addnstr(curses.LINES-2-spot, 0, "> ", START_CURSOR_X)

    stdscr.addstr(curses.LINES-1, 0, "> " + input_str)
    stdscr.refresh()

def main(stdscr):
    input_string = ""
    cursor_x = START_CURSOR_X
    cursor_y = curses.LINES-1
    global spot

    def draw():
        draw_scr(stdscr, input_string)

    draw()

    while True:
        stdscr.move(cursor_y, cursor_x)
        ch_code = stdscr.getch()
        ch = chr(ch_code)
        if ch_code == curses.KEY_UP:
            spot = min(len(tweet_arr)-1, spot + 1)
        elif ch_code == curses.KEY_DOWN:
            spot = max(0, spot - 1)
        elif ch_code == 8 or ch_code == 127:
            cursor_x = max(START_CURSOR_X, cursor_x - 1)
            input_string = input_string[:-1]
        elif ch_code == 10:
            # enter key
            break
        elif ch in string.printable and cursor_x < curses.COLS-1:
            cursor_x += 1
            input_string += ch

        # MUST UPDATE THE SPOT HERE!
        # THEN DRAW!!!
        tl = len(tweet_arr) - 1
        if tl < 0:
            spot = -1
        else:
            spot = min(tl, max(0, spot))

        draw()

wrapper(main)

if spot >= 0:
    print(tweet_arr[spot])
