# DWIN_T5UIC1_LCD

## Python class for the Ender 3 V2 LCD runing klipper3d with Moonraker 

https://www.klipper3d.org

https://docs.mainsail.xyz/

https://github.com/dw-0/kiauh

https://github.com/arksine/moonraker

https://github.com/raspberrypi/utils/tree/master/pinctrl


## Setup:

I installed Klipper, Moonraker and Mainsail via the Kiauh helper script. I would assume this all works with Fluidd and manual installs, the API key locations may change. *If you don't install a web front end like Mainsail/Fluidd, you'll need to enable the Klipper API.*
    
Reference [Klipper Docs.](https://www.klipper3d.org/API_Server.html)

You can access the Moonraker API via this shell command:
``` 
~/moonraker/scripts/fetch-apikey.sh
```
Or URL:
```
http://klipper.local:80/access/api_key
```

### [Disable Linux serial console](https://www.raspberrypi.org/documentation/configuration/uart.md)
  By default, the primary UART is assigned to the Linux console. If you wish to use the primary UART for other purposes, you must reconfigure Raspberry Pi OS. This can be done by using raspi-config:

  * Start raspi-config:
      ```
      sudo raspi-config
      ```
  * Select option 3 - Interface Options.
  * Select option P6 - Serial Port.
  * At the prompt Would you like a login shell to be accessible over serial? answer 'No'
  * At the prompt Would you like the serial port hardware to be enabled? answer 'Yes'
  * Exit raspi-config and reboot the Pi for changes to take effect.
  
  For full instructions on how to use Device Tree overlays see [this page](https://www.raspberrypi.org/documentation/configuration/device-tree.md). 

### Library requirements 

  Thanks to [wolfstlkr](https://www.reddit.com/r/ender3v2/comments/mdtjvk/octoprint_klipper_v2_lcd/gspae7y)

  ``` 
  sudo apt-get install python3-pip python3-gpiozero python3-serial git
  ```
  
  pip now requires a switch if the repository is not in 'apt install python3-xyz' on RPi for Bookworm when installing multitimer.
    *if there is a better solution that is up to date, please let me know :)
  ``` 
  sudo pip3 install multitimer --break-system-packages
  ```
  
  RPi.GPIO is depcrecated, use rpi-lgpio now, no code changes required.
  ``` 
  sudo apt install python3-rpi-lgpio
  ```

```
git clone https://github.com/idydxu/DWIN_T5UIC1_LCD.git
```

Enter the downloaded DWIN_T5UIC1_LCD folder.
```
cd ~/DWIN_T5UIC1_LCD
```

To confirm the GPIO of your board, run test_gpio.py.
```
sudo python3 ./test_gpio.py
```

### Wire the display 
  * Display <-> Raspberry Pi GPIO BCM
  * Rx  =   GPIO14  (Tx)
  * Tx  =   GPIO15  (Rx)
  * Ent =   GPIO13
  * A   =   GPIO19
  * B   =   GPIO26
  * Vcc =   2   (5v)
  * Gnd =   6   (GND)    

*Per SuperPi911's Repo
Here's a diagram based on my color selection:

<img src ="images/GPIO.png?raw=true" width="325" height="75">
<img src ="images/panel.png?raw=true" width="325" height="180">

I tried to take some images to help out with this: You don't have to use the color of wiring that I used:

<img src ="images/wire1.png?raw=true" width="200" height="400"> <img src ="images/wire2.png?raw=true" width="200" height="400">

<img src ="images/wire3.png?raw=true" width="400" height="200">

<img src ="images/wire4.png?raw=true" width="400" height="300">

### Run The Code

Run with    
```
sudo python3 ./run.py
```
 
```ctrl-c to exit```

# Run at boot:

`Note: Delay of 30s after boot to allow webservices to settle.

path of `run.py` is expected to be `~/DWIN_T5UIC1_LCD/run.py``

  ```
  sudo sed -i "s/USER=/USER=$(whoami)/" ./simpleLCD.service
  ```
   ```
   sudo chmod +x run.py
   ```   
   ```
   sudo chmod +x simpleLCD.service
   ```   
   ```
   sudo mv simpleLCD.service /lib/systemd/system/simpleLCD.service
   ```      
   ```
   sudo chmod 644 /lib/systemd/system/simpleLCD.service
   ```      
   ```
   sudo systemctl daemon-reload
   ```      
   ```
   sudo systemctl enable simpleLCD.service
   ```      
   ```
   sudo reboot
   ```
   
   

# Status:

## Working:

 Print Menu:
 
    * List / Print jobs from OctoPrint / Moonraker
    * Auto swiching from to Print Menu on job start / end.
    * Display Print time, Progress, Temps, and Job name.
    * Pause / Resume / Cancle Job
    * Tune Menu: Print speed & Temps

 Perpare Menu:
 
    * Move / Jog toolhead
    * Disable stepper
    * Auto Home
    * Z offset (PROBE_CALIBRATE)
    * Preheat
    * cooldown
 
 Info Menu
 
    * Shows printer info.

## Notworking:
    * Save / Loding Preheat setting, hardcode on start can be changed in menu but will not retane on restart.
    * The Control: Motion Menu
