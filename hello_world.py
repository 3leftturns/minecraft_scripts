from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

mc.postToChat("Hello Dylan & Sydney!")

x, y, z = mc.player.getPos()

#mc.postToChat("X: " + str(x) + " Y: " + str(y) + " Z: " + str(z))

#mc.player.setPos(-30,3,6)

for i in range (0,10):
  mc.setBlock(x,y + i, z, 10)
  sleep(10)
