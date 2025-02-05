enemies = 2  # this variable is different from the one which is inside increse_enemies() function

def increase_enemies():
    # if we want to modify global enemies varable inside this function
    # enemies = 1
    global enemies
    enemies += 1
    print(f"enemies inside function {enemies}")

increase_enemies()
print(enemies)