color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

print(all(i == 'green' for i in color1))
print(all(i == 'green' for i in color2))