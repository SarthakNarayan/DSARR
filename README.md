# DSARR

Supports ROS framework and is interfaced using a joystick 
Boards involved are Arduino and RaspberryPi

Running the code from computer:
To run the code first upload the code to arduino from the computer. 
Select the port carefully can be /dev/ttyACM0 or /dev/ttyACM1. Make this change 
in the python file.
Once the code has been uploaded run the python file while the arduino is plugged in.

OS for Raspberry Pi used:- UbuntuMate
Running from raspberry pi:
Just plug the arduino to raspberry pi. No need of arduino to be installed in Raspberry pi.
Go to command line and type
>lsusb
To see if arduino is recognized or not
> demsg | grep tty 
This is find out if the port connected to arduino is ttyACM0 or ttyACM1

Once the port is found out make the changes to the python file and run it.
