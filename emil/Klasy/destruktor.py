# 1 przyklad gdy najpierw zadziala print -> koniec , a dopiero pozniej __del__
class Destruktor:
    def __del__(self):
        print("koniec zycia")

obj = Destruktor()
print('koniec')

# 2 przyklad gdy zadziala najpierw __del__ a pozniej print-> koniec

class Destruktor:
    def __del__(self):
        print("koniec zycia")

obj = Destruktor()
del obj
print('koniec')