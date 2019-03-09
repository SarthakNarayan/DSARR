import pygame
import serial
import time

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init() 

arduinoData = serial.Serial('/dev/ttyACM0' , 9600)
time.sleep(2)
while True:
  #  print(str(arduinoData.readline()))
    pygame.event.pump()
    
    L1 = joystick.get_button(4)
    L2 = joystick.get_axis(2)
    R1 = joystick.get_button(5)
    R2 = joystick.get_axis(5)
    
    if L2 > 0.8:
        L2 = 1
    else: 
        L2 = 0

    if R2 > 0.8:
        R2 = 1
    else: 
        R2 = 0        

    init = joystick.get_button(7)
    quick_turn = joystick.get_button(9)
    mode_1 = joystick.get_button(0)
    mode_2 = joystick.get_button(2)
    mode_3 = joystick.get_button(3)
    mode_4 = joystick.get_button(1)
    mode_5 = joystick.get_button(10)
    arc = joystick.get_button(6)

    forward = joystick.get_axis(1)
    steer = joystick.get_axis(0)

    forward = (int((forward+1)/2 * 256))
    steer = (int((steer+1)/2 * 256))

    # Using Hat Buttons
    a,b = joystick.get_hat(0)
    if((a==-1) & (b==0)):
        LeftHat = 1
    else:
        LeftHat = 0
    if((a==0) & (b==1)):
        TopHat = 1
    else:
        TopHat=0
    if((a==0) & (b==-1)):
        BottomHat = 1
    else:
        BottomHat = 0
    if((a==1) & (b==0)):
        RightHat = 1 
    else:
        RightHat = 0   

    s= str(L1) + '\t' + str(L2) + '\t' + str(R1) + '\t' + str(R2) + '\t' + str(forward) + '\t' + str(steer) + '\t' + str(init) + '\t' + str(quick_turn) + '\t' + str(mode_1) + '\t' + str(mode_2) + '\t' + str(mode_3) + '\t' + str(mode_4) + '\t' + str(mode_5) + '\t' + str(arc) + '\t' + str(LeftHat) + '\t' + str(RightHat) + '\t' + str(TopHat) + '\t' + str(BottomHat) + '\n'
        
    arduinoData.write(s.encode())
    time.sleep(0.03)
