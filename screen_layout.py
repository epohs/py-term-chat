#!/usr/bin/env python

import curses
import time
from pprint import pprint

screen = curses.initscr()

try:
	(h, w) = screen.getmaxyx()


	#curses.noecho()
	curses.echo()
	curses.cbreak()
	curses.start_color()
	curses.use_default_colors()

	chat = curses.newpad(10000, w)
	input_window = curses.newwin(3, w, int(h-3), 0)
	
	#input_window.box()




	in_str = ''
	ins_row = 0
	scroll_top = 0


	while 1:
		c = input_window.getch()
		if c == curses.KEY_ENTER or c == 10 or c == 13:

			if ins_row >= int(h-3):
				scroll_top += 1

			chat.addstr(ins_row, 0, 'me: ')
			chat.addstr(ins_row, 4, in_str.encode('utf_8'), curses.A_DIM)
			chat.addstr(ins_row+1, 0, 'them: ', curses.A_BOLD)

			chat.refresh(scroll_top, 0, 0, 0, int(h-3), w)
			input_window.erase()
			in_str = ''
			ins_row += 1
		else:
			# Add this character to the string that 
			# we will insert later
			in_str += chr(c).encode('utf_8')


except KeyboardInterrupt:
	pass
finally:
	screen.keypad(0)
	curses.echo()
	curses.nocbreak()
	curses.endwin()