# 2.1
sheep_size = [5, 7, 300, 90, 24, 50, 75]
print("my name is Sơn and there are my sheep size:")
print(sheep_size)
# 2.2
def shear_max_sheep():
    max_sheep = max(sheep_size)
    print("now my biggest sheep has size {0} let's shear it ".format(max_sheep))
    # 2.3
    sheep_no = 0
    for item in sheep_size:
        if item == max_sheep:
            sheep_size[sheep_no] = 8
        sheep_no += 1
    print('after shearing ,here is my flock')
    print(sheep_size)
shear_max_sheep()

# 2.4
def month():
    global sheep_size
    sheep_size = [sheep + 50 for sheep in sheep_size]
    print("1 month has passed, now here is my flock")
    print(sheep_size)
month()
shear_max_sheep()
#2.5
n=4
for i in range(n):
    print("MONTH {0}:".format(i+1))
    month()
    shear_max_sheep()
#2.6
total_flock = sum(sheep_size)
print("my flock has size in total: {0} ".format(total_flock))
money = total_flock * 2
print("i would get {0} x 2$ = {1}$".format(total_flock,money))