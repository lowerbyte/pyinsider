import curses


class Canvas:

    def __init__(self, nrows: int, ncols: int):
        self._pad = curses.newpad(nrows, ncols)
        self._size = (nrows, ncols)

    @property
    def y(self):
        return self._pad_y

    @y.setter
    def y(self, y: int):
        self._pad_y = y

    @property
    def x(self):
        return self._pad_x

    @x.setter
    def x(self, x: int):
        self._pad_x = x

    @property
    def pad(self):
        return self._pad

    @property
    def size(self):
        return self._size

    # lu stands for left upper, rl stands for right lower
    # see documentation of refresh in curses
    def refresh(self,  luy: int, lux: int, rly: int, rlx: int):
        # LINES-2 due to hmi window (responsible for getting user input)
        self.pad.refresh(self.y, self.x, luy, lux, rly, rlx)
