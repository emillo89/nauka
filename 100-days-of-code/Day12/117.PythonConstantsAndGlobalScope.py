################### Scope ####################
#

# Modifying Global Scope
enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")



def increase_enemies2():
  return enemies + 1

enemies = increase_enemies2()
print(f"enemies outside function: {enemies}")

# Global Constants (You write UPPERCASE)

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

def calc():
    print(PI)

calc()