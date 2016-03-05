#example script to test 2 cascaded shift registers
#turns one pin on each loop


# Wipy pin	595 Pin
# 0			12
# 4			11
# 5			14

from ShiftReg import ShiftRegister
import time

srRows = ShiftRegister("GP0","GP4","GP5")


displayData = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

time.sleep_ms(3000)
for test in range(8):
	srRows.shiftOut(1<<test, False)
	srRows.shiftOut(1<<test, True)
	time.sleep_ms(500)
	
#turn shift registers off
srRows.shiftOut(0, False)
srRows.shiftOut(0, True)