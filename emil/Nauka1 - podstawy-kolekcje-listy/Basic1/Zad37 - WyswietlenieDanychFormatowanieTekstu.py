def personal_details():
    name,age = 'Simon',19
    address = "Bangalore, Karnataka, India"
    print('Name: {}, \nAge: {} , \nAddress: {}'.format(name,age,address))


personal_details()

# przyklad formatowanie na przykladzie dzialania matematycznego

x, y = 4, 3
result = x * x + 2 * x * y + y * y
print('({}+{})^2 = {}'.format(x,y,result))