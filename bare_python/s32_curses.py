#!python3

import curses
import traceback


def main(stdscr):
    # Frame the interface area at fixed VT100 size
    global screen
    screen = stdscr.subwin(23, 79, 0, 0)
    screen.box()
    screen.hline(2, 1, curses.ACS_HLINE, 77)
    screen.refresh()

    while True:
        pass


scr = curses.initscr()
try:
    # start curses app
    curses.noecho()
    curses.cbreak()
    scr.keypad(1)

    main(scr)

    # close curses app
    scr.keypad(0)
    curses.nocbreak()
    curses.echo()
    curses.endwin()

except Exception:
    # close curses app
    scr.keypad(0)
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    print(traceback.print_exc())
