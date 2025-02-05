# global scope
player_health = 10          # global variable, accessed anywhere

# local scope
def drink_potion():
    potion_strength = 2     # Local variable, accessed within function
    print(player_health)

drink_potion()

# this concept doesn't only apply on variable, it is application for fucntions as well