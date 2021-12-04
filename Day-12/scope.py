enemies = 1

def increase_enemies():
    enemies = 2
    print("Enemies inside this functions: {}".format(enemies))

increase_enemies()
print("Enemies outisde the function: {}".format(enemies))