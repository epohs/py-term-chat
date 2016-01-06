#!/usr/bin/env python

import curses
import curses.textpad
import time
from pprint import pprint

screen = curses.initscr()

try:
	(h, w) = screen.getmaxyx()

	curses.noecho()
	#curses.echo()


	chat = curses.newwin(h, w, 0, 0)
	input_window = curses.newwin(3, w, int(h-3), 0)
	
	input_window.box()
	#tb = curses.textpad.Textbox(input_window)
	#text = tb.edit()
	#curses.addstr(4,1,dims.encode('utf_8'))

	#hw = "Hello world!"

	in_str = ''

	while 1:
		c = input_window.getch()
		if c == curses.KEY_ENTER or c == 10 or c == 13:
			chat.addstr(0, 0, in_str.encode('utf_8'))
			chat.refresh()
			screen.erase()
		else:
			in_str += chr(c).encode('utf_8')
			chat.insch(0, (w-1), c)
			chat.refresh()


except KeyboardInterrupt:
	pass
finally:
	screen.keypad(0)
	curses.echo()
	curses.nocbreak()
	curses.endwin()