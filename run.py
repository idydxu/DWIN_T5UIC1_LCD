#!/usr/bin/env python3
import sys
import os
from dwinlcd import DWIN_LCD

#pass user through from bash command or local user if running manually
if len(sys.argv)>1:
    user = str(sys.argv[1])
else:
    user = input("Enter User: ")

# Change pins if you do not wire to the ReadMe
encoder_Pins = (26, 19) # For Ender3 v2
#encoder_Pins = (19,26) # For Other Displays, inverts dial encoder

button_Pin = 13
LCD_COM_Port = '/dev/ttyAMA0'
API_Key = 'XXXXXX' #See readme for how to access

DWINLCD = DWIN_LCD(
	LCD_COM_Port,
	encoder_Pins,
	button_Pin,
	API_Key,
    	user
)
