#!/usr/bin/env python3

from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

x, y, z = mc.player.getPos()

lava = 10
tnt = 46

def hellfire():
  mc.setBlock(x, y, z, lava)

def hellbelow():
  mc.setBlock(x,y,z-1, lava)

##hellfire() 
hellbelow()
