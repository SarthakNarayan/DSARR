import pygame
import serial
import time

offset_back_left = 18
offset_back_right = 30

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init() 

arduinoData = serial.Serial('/dev/ttyACM1' , 9600)
time.sleep(2)

while True:
    pygame.event.pump()
    
    numberA = joystick.get_button(0)
    numberB = joystick.get_button(1)
    numberX = joystick.get_button(2)
    numberY = joystick.get_button(3)
 
    analog = joystick.get_axis(1)
    #analog = int(((analog+1)/2.5 * 180))
    analog_left_back = (int(((analog+1)/2 * 180)) - offset_back_left)
    analog_right_back = 180 - (int(((analog+1)/2 * 180))) + offset_back_right

    #analog_left_back = int(((analog+1)/2.5 * 180)) 
    #analog_right_back = 180 - int(((analog+1)/0.66 * 180)) 

    print(analog_right_back)
    s= str(numberA) + '\t' + str(numberB) + '\t' + str(numberX) + '\t' + str(numberY) + '\t' + str(analog_left_back) +  '\t' + str(analog_right_back) + '\n'
    arduinoData.write(s.encode())
