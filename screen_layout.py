#!/usr/bin/env python

import curses
import time
from pprint import pprint



class ScreenLayout():


	def __init__(self):

		screen = curses.initscr()

		try:
			(self.h, self.w) = screen.getmaxyx()

			#curses.noecho()
			curses.echo()
			curses.cbreak()
			curses.start_color()
			curses.use_default_colors()

			self.chat = curses.newpad(10000, self.w)
			self.input_window = curses.newwin(3, self.w, int(self.h-3), 0)
			
			self.captureInput()


		except KeyboardInterrupt:
			pass
		finally:
			screen.keypad(0)
			curses.echo()
			curses.nocbreak()
			curses.endwin()




	def captureInput(self):

		in_str = ''
		ins_row = 0
		scroll_top = 0

		while 1:
			c = self.input_window.getch()
			if c == curses.KEY_ENTER or c == 10 or c == 13:

				if ins_row >= int(self.h-3):
					scroll_top += 1

				self.chat.addstr(ins_row, 0, 'me: ')
				self.chat.addstr(ins_row, 4, in_str.encode('utf_8'), curses.A_DIM)
				self.chat.addstr(ins_row+1, 0, 'them: ', curses.A_BOLD)

				self.chat.refresh(scroll_top, 0, 0, 0, int(self.h-3), self.w)
				self.input_window.erase()
				in_str = ''
				ins_row += 1
			else:
				# Add this character to the string that 
				# we will insert later
				in_str += chr(c).encode('utf_8')







