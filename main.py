from timeit import default_timer as timer
from datetime import timedelta
import pyautogui as pag
import random
import time
import math
import inquirer

movements = ['random', 'back and forth', 'circular']
questions = [inquirer.List('movement', message="Which mouse movement to do prefer?", choices=movements, ), ]
answer = inquirer.prompt(questions)
movement = answer['movement']
# random_movement = random.choice(movements)
# movement = random_movement
speed = 0.4
sleeping = 10
runs = 0

print('Your mouse is now moving in a ' + movement + ' motion with a ' + str(
    sleeping) + ' seconds delay between movements. To stop the script you press "Control" - "C".\n')

time.sleep(3)
start = timer()


def outcome():
    global runs
    runs += 1
    end = timer()
    time_diff = timedelta(seconds=end - start)
    print('This code has been running ' + str(runs) + ' times for ' + str(time_diff) + '.')
    time.sleep(sleeping)


if movement == 'random':
    while True:
        x = random.randint(600, 700)
        y = random.randint(200, 600)
        pag.moveTo(x, y, speed)
        outcome()
        '''end = timeit.timeit()
        print('This code has been running ' + str(runs) + ' times for ' + str(end - start) + '.')
        time.sleep(sleeping)'''


elif movement == 'back and forth':
    while True:
        x = 200
        y = x
        moves = 3
        for i in range(moves):
            pag.move(x, -y, speed)
            pag.move(-x, y, speed)
        outcome()


elif movement == 'circular':
    while True:

        radius = 5
        for i in range(360):
            if i % 6 == 0:
                pag.move(radius * math.cos(math.radians(i)), radius * math.sin(math.radians(i)))
        outcome()
