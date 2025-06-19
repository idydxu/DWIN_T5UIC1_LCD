#!/usr/bin/env python3
from dwinlcd import DWIN_LCD

# Change pins if you do not wire to the ReadMe
encoder_Pins = (26, 19) # For Ender3 v2
#encoder_Pins = (19,26) # For Other Displays, inverts dial encoder
button_Pin = 13
LCD_COM_Port = '/dev/ttyAMA0'
API_Key = 'XXXXXX' #API key for Moonraker/Moonsail can be found at http://<klipper host>/access/api_key

DWINLCD = DWIN_LCD(
	LCD_COM_Port,
	encoder_Pins,
	button_Pin,
	API_Key
)
