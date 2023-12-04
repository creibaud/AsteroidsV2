import pygame
import random
import math
import components.SpaceShip as SpaceShip

def setUp():
    SpaceShip.setUp()

def update():
    SpaceShip.update()

def rotateSpaceShip(angle):
    SpaceShip.rotate(angle)

def spaceShipAccelerate(isAcceleration):
    if isAcceleration:
        SpaceShip.accelerate()
    else:
        SpaceShip.decelerate()

def shootSpaceShip():
    SpaceShip.shoot()

def draw():
    SpaceShip.draw((255, 255, 255))
    SpaceShip.Bullets.draw()
