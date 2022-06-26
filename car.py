
# Write your code here :-)
#from gpiozero import Robot
import RPi.GPIO as GPIO
from time import sleep
import os


#Roberta = Robot((6,13),(19,26))
#Roberta.forward(0.8)
#sleep(10)
#Roberta.stop()

# from gpiozero import Motor
from gpiozero import Robot
from bluedot import BlueDot

bd = BlueDot()
robot = Robot(left=(6, 13), right=(19, 26))

#MotorL = Motor(6, 13)
#MotorR = Motor(19, 26)

def move(pos):
  if pos.top:
      #MotorL.forward()
      #MotorR.forward()
      robot.forward()
  elif pos.bottom:
      #MotorL.backward()
      #MotorR.backward()
      robot.backward()
  elif pos.right:
      robot.right()
  elif pos.left:
      robot.left()
      
      
def stop():
    robot.stop()

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

os.system('sleep 10s')
os.system('python iotscript.py')
      
      

#MotorL.forward()
#MotorR.forward()
#sleep(5)
#MotorL.stop()
#MotorR.stop()
