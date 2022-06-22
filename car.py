#test
# Write your code here :-)
#from gpiozero import Robot
import RPi.GPIO as GPIO
from time import sleep

#Roberta = Robot((6,13),(19,26))
#Roberta.forward(0.8)
#sleep(10)
#Roberta.stop()

from gpiozero import Motor

MotorL = Motor(6, 13)
MotorR = Motor(19, 26)

MotorL.forward()
MotorR.forward()
sleep(5)
MotorL.stop()
MotorR.stop()
