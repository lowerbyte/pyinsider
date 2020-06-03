import curses
import logging
from core.canvas import Canvas


def main(stdscr):
    code_view = Canvas(500, 500)
    frame_view = Canvas(500, 500)

    # split screen
    stdscr.vline(0, curses.COLS//2, '|', curses.LINES-2)

    stdscr.refresh()
    stdscr.getch()


if __name__ == '__main__':
    logging.basicConfig(filename='pyinsider.log')
    curses.wrapper(main)
