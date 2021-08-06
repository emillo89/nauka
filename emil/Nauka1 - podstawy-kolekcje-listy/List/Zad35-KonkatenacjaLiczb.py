my_list = ['p', 'q']
n = 4

# w taki sposob wyswuetli nam najpierw p1,q1,p2,q2 itp
new_list = ['{}{}'.format(x,y) for y in range(1,n+1) for x in my_list]
print(new_list)

# w taki sposob wyswuetli nam najpierw p1,p2,p3,p4,q1,q1...
new_list = ['{}{}'.format(x,y) for x in my_list for y in range(1,n+1)]
print(new_list)

