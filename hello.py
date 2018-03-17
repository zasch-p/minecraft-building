from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# Current posistion
player_x, player_y, player_z  = mc.player.getTilePos()

def bulldozer(x, y, z):
    mc.setBlocks(x - 27, y, z - 30, x + 30, y + 20, z + 30, 0)

def buildWall(x, y, z):
    mc.setBlocks(x, y, z, x + 20, y + 10, z, 5)

# Build things
# bulldozer(player_x, player_y, player_z)

buildWall(player_x + 2, player_y, player_z + 2)
