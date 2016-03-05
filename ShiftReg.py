#!/usr/bin/env python3

# Micropython library for the WiPy for 595 shift registers
# I needed a bit more GPIO than the device had
# Copyright (c) 2016, Christopher Berg

# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from machine import Pin
import time

class ShiftRegister:
	#need to know what pins we're using
	#On DIP 595 - pins 12, 11 an 14
	def __init__(self, latch, clock, data):
		self._latch = latch
		self._clock = clock
		self._data = data
		self._latchPin = Pin(latch, mode=Pin.OUT)
		self._latchPin.value(0)
		self._clockPin = Pin(clock, mode=Pin.OUT)
		self._clockPin.value(1)
		self._dataPin = Pin(data, mode=Pin.OUT)
		self._dataPin.value(0)
		
	def shiftOut(self, data, latch=True):
		# print(data)
		for bit in range(8):
			print(bit)
			
			if 0 == (data & (1<<bit)):
				self._dataPin.value(0)
				print("low")
			else:
				self._dataPin.value(1)
				print("high")
			self._clockPin.value(0)
			time.sleep_us(1)
			self._clockPin.value(1)
			time.sleep_us(10)
		if(latch):
			self._latchPin.value(0)
			time.sleep_us(1)
			self._latchPin.value(1)
			time.sleep_us(1)