from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# Current posistion
player_x, player_y, player_z  = mc.player.getTilePos()

def bulldozer(x, y, z):
    mc.setBlocks(x - 27, y, z - 30, x + 30, y + 20, z + 30, 0)

# Build things
bulldozer(player_x, player_y, player_z)

